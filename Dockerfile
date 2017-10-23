FROM camptocamp/c2cwsgiutils:0

EXPOSE 80
RUN pip install ldap3
WORKDIR /app
COPY . /app

RUN python ./setup.py install && \
    flake8 internal_healthchecks
