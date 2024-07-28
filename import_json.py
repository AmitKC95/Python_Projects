import json
import os

# Define the data to be written to the JSON file
data = {
    "scores": [100, 90, 80]
}

# Define the directory and filename
directory = "game_folder"
filename = "top_scores.json"

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the full path to the JSON file
filepath = os.path.join(directory, filename)

# Write the data to the JSON file
with open(filepath, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON file created at: {filepath}")
