import urllib.request
import json
import codecs

#Your API here
locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'

api_key = locu_api
url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
html =  urllib.request.urlopen(url)
#print(html.read())

def locu_search(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib.request.urlopen(final_url)
    reader = codecs.getreader("utf-8")
    data = json.load(reader(json_obj))
   
    for item in data['objects']:
        print(item['name'], item['phone'])


#Sample Query
locu_search('New York')
