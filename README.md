# django\_underpants

These are some stupid-simple helper classes to integrate [Django]'s
authentication systems with [Underpants] for intranet single-signon via Google
Apps OAuth.

Once installed, add the following to your `settings.py` to use the new classes.

```python
MIDDLEWARE_CLASSES += (
    "django_underpants.UnderpantsRemoteUserMiddleware",
)


AUTHENTICATION_BACKENDS = (
    "django_underpants.UnderpantsRemoteUserBackend",
)
```

[Django]: https://github.com/django/django
[Underpants]: https://github.com/kellegous/underpants/
