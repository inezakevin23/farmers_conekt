import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    kwargs = {}
    if os.getenv('DB_SSL', '').lower() in ('1', 'true', 'yes'):
        kwargs['ssl'] = {'ca': None}
        kwargs['ssl_verify_cert'] = False

    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT', '3306')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor,
        **kwargs
    )

    return connection