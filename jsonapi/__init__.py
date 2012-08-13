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
    parser.add_argument('url')
    parser.add_argument('data', nargs='?')
    parser.add_argument('-m', '--method', choices=['GET', 'POST'], default='GET')
    parser.add_argument('-v', '--version', default='2010')
    parser.add_argument('-s', '--sid', default=os.getenv("TWILIO_ACCOUNT_SID"))
    parser.add_argument('-t', '--token', default=os.getenv("TWILIO_AUTH_TOKEN"))
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

    #url = "".join(["https://api.twilio.com", url])
    url = "".join(["http://api.local.twilio.com:4567", url])
    response = getattr(requests, method)(
        url, data=data, auth=(sid, token),
        headers={'Accept': 'application/json'})

    a = json.loads(response.content)
    pprint.pprint(a, indent=4)

def main():
    args = load_args()
    make_request(args.url, args.version, args.method.lower(), args.data,
                 args.sid, args.token)

if __name__ == "__main__":
    main()

