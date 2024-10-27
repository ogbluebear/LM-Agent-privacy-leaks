import json

# Load the JSON data from a file
with open('gpt_evaluate_outputs/Original_EvalOutput.json', 'r') as file:
    data = json.load(file)

# Initialize an empty list to store entries with "leak_info" set to true
leaked_entries = []

# Loop through each entry in the JSON data
for entry_name, entry_data in data.items():
    if entry_data.get("leak_info"):  # Check if "leak_info" is True
        leaked_entries.append(entry_name)

# Print the list of entries with leak_info as True
print("Entries with 'leak_info' as True:", leaked_entries)