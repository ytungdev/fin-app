import json
import os
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


with open(os.path.join(settings.BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(item, secrets=secrets):
    """Get secret {item} or fail with ImproperlyConfigured"""
    try:
        return secrets[item]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))