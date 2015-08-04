from setuptools import setup

setup(
    name="django_underpants",
    description="Django authentication bits for use with Underpants.",
    version="1.0",
    author="Neil Williams",
    author_email="neil@reddit.com",
    py_modules=["django_underpants"],
    install_requires=[
        "django",
    ],
)
