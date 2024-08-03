import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python script_name.py <search_term>")

search_term = sys.argv[1]
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={search_term}")

response_json = response.json()

print(json.dumps(response_json, indent=2))

if "results" in response_json:
    for result in response_json["results"]:
        # Access 'trackName' using square brackets
        print(result["trackName"])
else:
    print("No results found.")
