import json
import urllib.request

url = input('Enter location: ')
data = urllib.request.urlopen(url).read()

print('Retrieving', url)
info = json.loads(data)

print('Retrieved', len(data), 'characters')

count = 0
total = 0

for item in info['comments']:
    count += 1
    total = total + item['count']

print('Count', count)
print('Sum', total)
