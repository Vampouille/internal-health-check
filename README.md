Internal Health Check
=====================

This repository holds code to check services that are not exposed on internet:
database, ldap server.

Currently it check postgres database and LDAP server. After running this
composition, you can check status of internel services with following URL :
(http://localhost:8080/api/c2c/health_check)

## Check database

In order to check database, just set following environment variables:

* **POSTGRES_CONNECTION_STRING**: configure connection to database:
```
host=db port=5432 dbname=test user=joe password=secret
```
* **POSTGRES_TEST_QUERY**: SQL query use to test db, this query should at
  least return one result

## Check LDAP server

To check LDAP server, just set following environment variable:
* **LDAP_TEST_URL**: Configure access and entry to search for with following format:
  ldap://*<login>*:*<password>*@*<hostname>*/*<ldap entry>*

Example :
```
ldap://cn=admin,dc=georchestra,dc=org:secret@ldap/uid=geoserver_privileged_user,ou=users,dc=georchestra,dc=org
```

LDAP_TEST_URL is composed of following parts:
* login: `cn=admin,dc=georchestra,dc=org` in previous example
* password: `secret` in previous example
* ldap hostname: `ldap` in previous example
* ldap entry to search for:
  `uid=geoserver_privileged_user,ou=users,dc=georchestra,dc=org` in previous
  example

This test works by searching one entry in LDAP. If such entry exists then test is
considered OK.

## Adding basic auth to protect health checks

You can protect health check status page by adding basic auth on it. For example
on HAProxy:

```
global
    ssl-default-bind-options no-sslv3
defaults
    timeout client 1200000
    timeout server 1200000
userlist health_check_user
  user health_check insecure-password secret
frontend http
    acl AuthOkay http_auth(health_check_user)
    acl Protected path_beg /public/test-auth/
    http-request auth realm Secure if !AuthOkay Protected
```
