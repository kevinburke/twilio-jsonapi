#!/usr/bin/env python
import argparse
import json
import os
import pprint
import re
import sys
import urlparse

import requests

def load_args(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(
        description="Parse some Json command line opts")
    parser.add_argument('url',
                        help='The URL to request, after /2010-04-01/Accounts/AC123')
    parser.add_argument('-X', '--method', choices=['GET', 'POST'],
                        default='GET', help='HTTP method to use')
    parser.add_argument('-d', '--data', choices=['GET', 'POST'],
                        default='GET', help='The body of a post request, if any')
    parser.add_argument('-v', '--version', default='2010',
                        choices=['2008', '2010'],
                        help='Twilio API version to use')
    parser.add_argument('-s', '--sid', default=os.getenv("TWILIO_ACCOUNT_SID"),
                        help=('Account Sid. Defaults to the TWILIO_ACCOUNT_SID'
                              ' environment variable'))
    parser.add_argument('-t', '--token', default=os.getenv("TWILIO_AUTH_TOKEN"),
                        help=('Auth Token. Defaults to the TWILIO_AUTH_TOKEN'
                              ' environment variable'))
    return parser.parse_args(args)

def add_json_to_path(url):
    if '.json' in url:
        return url

    url_parts = urlparse.urlparse(url)
    new_path = url_parts.path + '.json'
    return urlparse.urlunparse(('', '', new_path, '', url_parts.query, ''))

def get_version(year):
    return '2008-08-01' if year == '2008' else '2010-04-01'

def make_request(url, year, method, data, sid, token):

    version = get_version(year)
    url = add_json_to_path(url)

    # skip the boring uri parts by default
    if not re.search('^/(2008-08-01|2010-04-01)/Accounts', url):
        url = "".join(['/', version, "/Accounts/", sid, url])

    url = "".join(["https://api.twilio.com", url])
    response = getattr(requests, method)(
        url, data=data, auth=(sid, token),
        headers={'Accept': 'application/json'})

    a = json.loads(response.content)
    pprint.pprint(a, indent=4)
    return response

def main():
    args = load_args()
    make_request(args.url, args.version, args.method.lower(), args.data,
                 args.sid, args.token)

if __name__ == "__main__":
    main()
