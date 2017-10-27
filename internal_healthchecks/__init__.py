import c2cwsgiutils.pyramid
from c2cwsgiutils.health_check import HealthCheck
from pyramid.config import Configurator
import os

from internal_healthchecks.ldap_check import check_ldap
from internal_healthchecks.postgres_check import check_postgres


def main(_, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, route_prefix='/api')
    config.include(c2cwsgiutils.pyramid.includeme)
    config.scan("internal_healthchecks.services")
    health_check = HealthCheck(config)
    if os.getenv("LDAP_TEST_URL", None) is not None:
        health_check.add_custom_check('check ldap', check_ldap, 2)
    if os.getenv("POSTGRES_CONNECTION_STRING", None) is not None:
        health_check.add_custom_check('check postgres', check_postgres, 2)

    return config.make_wsgi_app()
