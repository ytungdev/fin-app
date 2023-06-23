import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured


load_dotenv()

def use_env(item):
    """Get secret {item} or fail with ImproperlyConfigured"""
    try:
        return os.getenv(item)
    except KeyError:
        raise ImproperlyConfigured("Set `{}` in .env".format(item))