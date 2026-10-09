# Farmer Conekt - media storage backends.
#
# Two backends are supported:
#   * local  (default) - images are written to the local upload folder.
#   * supabase - images are uploaded to a Supabase Storage bucket.
#
# Configure the backend with the MEDIA_BACKEND environment variable.
# The `supabase` package is only imported when the Supabase backend is enabled.

import os
import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = BASE_DIR / 'uploads' / 'crop_images'

MEDIA_BACKEND = os.getenv('MEDIA_BACKEND', 'local').lower()

SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', '')
SUPABASE_BUCKET = os.getenv('SUPABASE_BUCKET', 'crop-images')

_client = None


def get_client():
    """Get the lazily created Supabase client (None unless Supabase backend is enabled)."""
    if MEDIA_BACKEND != 'supabase':
        return None
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        raise RuntimeError(
            'Supabase storage is enabled but SUPABASE_URL / SUPABASE_ANON_KEY are missing. '
            'Create a bucket and set the env vars in your deployment environment.'
        )
    global _client
    if _client is None:
        from supabase import create_client
        _client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    return _client


def upload_media(file_bytes: bytes, filename: str, content_type: str):
    """Upload an image and return (storage_path, public_url)."""
    if MEDIA_BACKEND == 'supabase':
        client = get_client()
        bucket = client.storage.from_(SUPABASE_BUCKET)
        object_name = f'{uuid.uuid4()}_{filename}'
        bucket.upload(
            object_name,
            file_bytes,
            file_options={'content_type': content_type},
        )
        public_url = bucket.get_public_url(object_name)
        return object_name, public_url

    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    object_name = f'{uuid.uuid4()}_{filename}'
    (UPLOAD_FOLDER / object_name).write_bytes(file_bytes)
    public_url = f'/uploads/crop_images/{object_name}'
    return object_name, public_url


def get_media_url(storage_path: str) -> str:
    """Return the publicly accessible URL for a stored media object."""
    if MEDIA_BACKEND == 'supabase':
        return storage_path
    return f'/uploads/crop_images/{storage_path}'
