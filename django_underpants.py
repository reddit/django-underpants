"""Authentication components for single-signon via Underpants."""

import urllib

from django.contrib.auth.middleware import RemoteUserMiddleware
from django.contrib.auth.backends import RemoteUserBackend


class UnderpantsRemoteUserMiddleware(RemoteUserMiddleware):
    header = "HTTP_UNDERPANTS_EMAIL"


class UnderpantsRemoteUserBackend(RemoteUserBackend):
    def clean_username(self, username):
        return urllib.unquote(username)
