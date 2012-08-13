#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "jsonapi",
    version = "0.1",
    description = "Twilio API shortcuts",
    author = "Kevin Burke",
    author_email = "kevin@twilio.com",
    packages = find_packages(),
    entry_points = {
        "console_scripts": [
            "jsonapi = jsonapi:main",
        ],
    }
)

