import requests
import sys
import json

if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))

o = response.json()
#for result in o["results"]:
#    print(result["trackName"])
print(o)
print(type(o))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

for k in o:
    print(k)
    #print(k," :: ",o[k])
print("#####################################################")
for j in o["results"]:
    print(j)
