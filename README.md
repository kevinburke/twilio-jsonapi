# JSONapi

JSONapi is a convenience wrapper for the Twilio API.

### Usage

```bash
# Set your account sid and auth token in your environment, so you don't have to
# enter them every time
export TWILIO_ACCOUNT_SID='AC1234'
export TWILIO_AUTH_TOKEN='cdef'

# Then retrieve a page of calls
jsonapi '/Calls?PageSize=1'
```

You'll get back pretty printed json like this:

```python
{   u'calls': [   {   u'account_sid': u'AC58f1e002b1c6b88ca90a012a4be0c',
                      u'annotation': None,
                      u'answered_by': None,
                      u'api_version': u'2010-04-01',
                      u'caller_name': None,
                      u'date_created': u'Sat, 11 Aug 2012 21:10:17 +0000',
                      u'date_updated': u'Sat, 11 Aug 2012 21:10:58 +0000',
                      u'direction': u'outbound-api',
                      u'duration': u'11',
                      u'end_time': u'Sat, 11 Aug 2012 21:10:58 +0000',
                      u'forwarded_from': None,
                      u'from': u'+14103920364',
                      u'from_formatted': u'(410) 392-0364',
                      u'group_sid': None,
                      u'parent_call_sid': None,
                      u'phone_number_sid': u'PN5fb9e7778e184c8baa86c1fb7544ca0f',
                      u'price': u'-0.02000',
                      u'sid': u'CAc56534caa45873571865df8b1ad20e35',
                      u'start_time': u'Sat, 11 Aug 2012 21:10:47 +0000',
                      u'status': u'completed',
                      u'subresource_uris': {   u'notifications': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls/CAc85f34caa4587aa70865df8b1ad20e35/Notifications.json',
                                               u'recordings': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls/CAc85f34caa4587aa70865df8b1ad20e35/Recordings.json'},
                      u'to': u'+19252717005',
                      u'to_formatted': u'(925) 271-7005',
                      u'uri': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls/CAc85f34caa4587aa70865df8b1ad20e35.json'}],
    u'end': 0,
    u'first_page_uri': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls.json?PageSize=1&Page=0',
    u'last_page_uri': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls.json?PageSize=1&Page=1108',
    u'next_page_uri': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls.json?PageSize=1&Page=1&AfterSid=CAc56534caa45873571865df8b1ad20e35',
    u'num_pages': 1109,
    u'page': 0,
    u'page_size': 1,
    u'previous_page_uri': None,
    u'start': 0,
    u'total': 1109,
    u'uri': u'/2010-04-01/Accounts/AC58f1e002b1c6b88ca90a012a4be0c/Calls.json?PageSize=1'}
```

Post new data:

```bash
jsonapi /SMS/Messages -m POST -d 'To=+14105551234&Body=Hi there'
```

By default the 2010 API is used. To use the 2008 API:

```bash
jsonapi /Calls -v 2008
```

## Installation

Clone this repository, then run:

```bash
python setup.py install
```

at the command line.
