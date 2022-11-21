""" Json Manipulaiton """

import json
import urllib.request
import time

def process():
    url= 'https://my.api.mockaroo.com/people.json?key=8ae639a0'
    print(f"Calling API... {url}")
    tic = time.time()
    response = urllib.request.urlopen(url)
    toc = time.time()
    print(f"API Response received in {toc-tic} seconds")
    #print(response.read())
    content = response.read()
    print(content)
    person_data = json.loads(content.decode('utf-8'))
    #print(json_data)
    for person in person_data:
        print(f"Name: {person['first_name']} {person['last_name']}, Email: {person['email']}")


process()