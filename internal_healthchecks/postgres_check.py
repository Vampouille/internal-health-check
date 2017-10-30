from pyramid.httpexceptions import HTTPInternalServerError
import psycopg2
import os


def check_postgres(_request):
    try:
        conn = psycopg2.connect(os.getenv('POSTGRES_CONNECTION_STRING'))
        cur = conn.cursor()
    except Exception:
        raise HTTPInternalServerError('Unable to connect to database')

    query = os.getenv('POSTGRES_TEST_QUERY',
                      'SELECT table_name FROM information_schema.tables;')

    try:
        cur.execute(query)

        # Check if test query returns some results
        if cur.rowcount < 1:
            raise HTTPInternalServerError('Empty result from test query')
        cur.close()
        conn.close()
    except Exception:
        raise HTTPInternalServerError('Unable to execute test query')
