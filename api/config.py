import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "a_very_long_secret_key_must_be_at_least_32_bytes_long_for_hmac256",
)
