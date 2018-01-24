#! /usr/bin/env python3

import requests
import feedparser
import lxml.html
import json

with open('config.json','r') as jsonfile:
    cfg = json.load(jsonfile)

URL = cfg['SERVER_URL'] + '/activity'
USER = cfg['USER']
PASS = cfg['PWD']

params = {'os_authType': 'basic', 'streams': 'user IS '+USER, 'maxResults': 200}
mylist = []

response = requests.get(URL, auth=(USER, PASS), params=params)

feed = feedparser.parse(response.content)

# print(feed['feed']['title'])

for entry in feed['entries']:
    app = entry['atlassian_application']
    try:
        link = lxml.html.fromstring(entry['link']).text_content().replace('\n', '#')
    except Exception:
        link = '!!!'
    try:
        summary = lxml.html.fromstring(entry['summary']).text_content().replace('\n', '#')
    except Exception:
        summary = '!!!'
    mylist.append(entry['updated'][1:10] + ' ' + link + ' ' + summary)
    # print(entry['activity_verb'])

mylist = reversed(sorted(set(mylist)))

for myline in mylist:
    print(myline)
