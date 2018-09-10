#!/usr/bin/env python
import requests
import urllib
import sys
import lxml.html as html
# from subprocess import check_output

want_tags = ['p','h1','h2','h3','div']
want_divs = ['variablelist','aws-note']

if len(sys.argv) < 2:
    print("usage:\ncfn_docs security group\ncfn_docs ec2")

feeling_lucky_url = 'https://www.google.com/search?btnI=1&q='
query = "aws cloudformation "

for arg in sys.argv[1:]:
    query += arg + " "

query = urllib.quote_plus(query.strip())
url = feeling_lucky_url + query
response = requests.get(url)
parsed = html.fromstring(response.text)
main_content = parsed.get_element_by_id("main-col-body")
content = html.tostring(main_content)
for el in main_content:
  if (el.tag not in want_tags) or \
     (el.tag == 'div') and not ( \
       ('class' in el.attrib.keys() and el.attrib['class'] in want_divs) or \
       ('id' in el.attrib.keys() and el.attrib['id'] in want_divs) 
     ):
    continue
  print(html.tostring(el))