import re
import os
import ldap3
from pyramid.httpexceptions import HTTPInternalServerError


def check_ldap(_request):
    """Check specified entry in ldap

    A configuration string should be present in LDAP_TEST_URL var with
    following format:
    ldap://user:password@server:port/uid=test,ou=users,dc=example,dc=com"""
    test_string = os.getenv("LDAP_TEST_URL", None)

    m = re.search('ldap://((.+):(.+)@)([^:]+)(:(\d+))?/([^,]+),(.+)',
                  test_string)
    if m is None:
        raise Exception("Invalid LDAP configuration")
    user = m.group(2)
    password = m.group(3)
    server = m.group(4)
    if m.group(6) is None:
        port = 389
    else:
        port = m.group(6)
    dn1 = m.group(7)
    dn2 = m.group(8)
    print('User: %s, Pass: %s, Server: %s, Port: %s, DN1: %s DN2: %s' %
          (user, password, server, port, dn1, dn2))

    conn = ldap3.Connection(ldap3.Server(server,
                                         port=port,
                                         get_info=ldap3.ALL),
                            user,
                            password,
                            auto_bind=True)
    if not conn.search(dn2, '(%s)' % dn1):
        raise HTTPInternalServerError(
            'Cannot find %s in LDAP' % dn1)
