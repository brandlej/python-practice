# import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}"
)

# pretty print
# print(json.dumps(response.json(), indent=2))

# return json of response
o = response.json()

# iterate over each entry in results
# list of songs in this case
for result in o["results"]:
    print(result["trackName"])
