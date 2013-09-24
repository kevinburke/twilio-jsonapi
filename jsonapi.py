#!/usr/bin/env python
"""
Convenience wrapper for accessing the Twilio API.

@author Kevin Burke <kev@inburke.com>
"""
import argparse
import json
import os
import re
import sys
import urlparse

import requests
from httpie.core import main as httpie


def load_args(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(
        description="Parse some Json command line opts")
    parser.add_argument('url',
                        help='The URL to request, after /2010-04-01/Accounts/AC123')
    parser.add_argument('-X', '--method', choices=['GET', 'POST'],
                        default='GET', help='HTTP method to use')
    parser.add_argument('-v', '--version', default='2010',
                        choices=['2008', '2010'],
                        help='Twilio API version to use')
    parser.add_argument('-s', '--sid', default=os.getenv("TWILIO_ACCOUNT_SID"),
                        help=('Account Sid. Defaults to the TWILIO_ACCOUNT_SID'
                              ' environment variable'))
    parser.add_argument('-t', '--token', default=os.getenv("TWILIO_AUTH_TOKEN"),
                        help=('Auth Token. Defaults to the TWILIO_AUTH_TOKEN'
                              ' environment variable'))
    parser.add_argument('-x', '--xml', action='store_true',
                        help=('Return XML response'))
    parser.add_argument('-d', '--data', dest='data', nargs=argparse.REMAINDER,
                        help='The body of a post request, if any')
    parser.add_argument('-i', '--include', action='store_true',
                        help='Include headers')
    return parser.parse_args(args)

def add_json_to_path(url):
    if '.json' in url:
        return url

    url_parts = urlparse.urlparse(url)
    new_path = url_parts.path + '.json'
    return urlparse.urlunparse(('', '', new_path, '', url_parts.query, ''))

def get_version(year):
    return '2008-08-01' if year == '2008' else '2010-04-01'

def make_request(url, year, method, data, sid, token, xml, include_headers):

    if not sid:
        raise ValueError("Please set a valid AccountSid as TWILIO_ACCOUNT_SID "
                         "in your environment, or by passing the --sid flag "
                         "at the command line.")

    if not token:
        raise ValueError("Please set a valid Auth Token as TWILIO_AUTH_TOKEN "
                         "in your environment, or by passing the --token flag "
                         "at the command line.")

    if not xml:
        url = add_json_to_path(url)

    # skip the boring uri parts by default
    if not re.search('^/(2008-08-01|2010-04-01)/Accounts', url):
        url = "".join(['/', get_version(year), "/Accounts/", sid, url])

    url = "".join(["https://api.twilio.com", url])

    httpie_args = [method.upper(), url]


    if method == 'post' and data is not None:
        httpie_args.insert(0, '-f') # -f is used to denote form values. must be inserted after '-b'
        data = ['{}={}'.format(key, value) for [key, value] in map(lambda x: x.split('='), data)]
        httpie_args.extend(data) # add data

    httpie_args.extend(['-a', '{}:{}'.format(sid, token)])

    if not include_headers:
        httpie_args.insert(0, '-b') # -b means only include response body

    httpie(httpie_args)

def main():
    args = load_args()
    make_request(args.url, args.version, args.method.lower(), args.data,
                 args.sid, args.token, args.xml, args.include)

if __name__ == "__main__":
    main()

