import os
import ssl

import pymysql
from dotenv import load_dotenv

load_dotenv()


def _load_ca():
    """Return CA certificate bytes from DB_SSL_CA (a file path or PEM content)."""
    ca = os.getenv('DB_SSL_CA', '').strip()
    if not ca:
        return None
    if os.path.isfile(ca):
        with open(ca, 'rb') as f:
            return f.read()
    return ca.encode('utf-8')


def get_db_connection():
    """Connect to MySQL (local or Aiven). DB_PORT defaults to 3306; Aiven needs TLS."""
    ssl_ctx = None
    if os.getenv('DB_SSL', '').lower() in ('1', 'true', 'yes', 'on'):
        ca_bytes = _load_ca()
        if ca_bytes is None:
            raise RuntimeError(
                'Aiven TLS is enabled (DB_SSL=true) but DB_SSL_CA is not set. '
                'Provide the Aiven CA certificate as DB_SSL_CA (path to ca.pem, '
                'or paste the PEM content directly).'
            )
        ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ssl_ctx.load_verify_locations(cadata=ca_bytes.decode('utf-8'))
        ssl_ctx.check_hostname = True
        ssl_ctx.verify_mode = ssl.CERT_REQUIRED

    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT', '3306')),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        cursorclass=pymysql.cursors.DictCursor,
        ssl=ssl_ctx,
    )
