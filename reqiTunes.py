import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# limit 50 above means 50 responses will come

o = response.json()
for result in o["results"]:
        print(result["trackName"])

# when executing code, type filename.py followed by,
# band you're searching, as sys.argv is used,
# which uses [1] place for input, [0] is filename
