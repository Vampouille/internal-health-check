from pyramid.httpexceptions import HTTPInternalServerError
import psycopg2
import os


def check_postgres(_request):
    conn = psycopg2.connect(os.getenv('POSTGRES_CONNECTION_STRING'))
    cur = conn.cursor()
    query = os.getenv('POSTGRES_TEST_QUERY',
                      'SELECT table_name FROM information_schema.tables;')

    cur.execute(query)

    # Check if test query returns some results
    if cur.rowcount < 1:
        raise HTTPInternalServerError('Empty result from test query')
    cur.close()
    conn.close()
