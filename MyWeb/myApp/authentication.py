"""
Django authentication backend.
"""

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django_python3_ldap import ldap


class LDAPBackend(ModelBackend):

    """
    An authentication backend that delegates to an LDAP
    server.
    User models authenticated with LDAP are created on
    the fly, and syncronised with the LDAP credentials.
    """

    supports_inactive_user = False

    def authenticate(self, *args, **kwargs):

        username = kwargs['username']
        password = kwargs['password']

        print(f" LDAPBackend ....{username} / {password}  ")
        user = ldap.authenticate(*args, **kwargs)
        print(user)
        return user


class MyLoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        print(request)
        print(f" MyLoginBackend username: {username},  password: {password} ")
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            user = User.objects.get(username='peter')

        # you must login request
        login(request, user)
        print(user.is_authenticated, request.user.is_authenticated)

        print(f"return {user}")
        return user
