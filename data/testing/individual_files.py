import json
import os

# Load the main data file
with open("../main_data.json", "r") as main_file:
    main_data = json.load(main_file)

# List of names to extract
selected_names = [
    'main91', 'main92', 'main95', 'main97', 'main98', 'main105', 'main113', 'main115', 'main119', 'main121',
    'main127', 'main141', 'main143', 'main154', 'main162', 'main168', 'main173', 'main176', 'main187', 'main191',
    'main196', 'main200', 'main204', 'main231', 'main242', 'main263', 'main266', 'main275', 'main277', 'main278',
    'main280', 'main281', 'main283', 'main290', 'main300', 'main302', 'main304', 'main305', 'main309', 'main329',
    'main336', 'main341', 'main345', 'main347', 'main358', 'main361', 'main362', 'main366', 'main371', 'main373',
    'main377', 'main380', 'main381', 'main388', 'main392', 'main398', 'main410', 'main411', 'main416',
    'main421', 'main423', 'main426', 'main430', 'main444', 'main453', 'main462', 'main468', 'main472', 'main476',
    'main480', 'main484', 'main492'
]

# Directory to save individual files
output_directory = "./"

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Extract and save each selected entry as a standalone JSON file
for entry in main_data:
    entry_name = entry.get("name")
    
    # Check if the entry's name is in the selected names list
    if entry_name in selected_names:
        # Define the file name for the individual JSON file
        output_file_path = os.path.join(output_directory, f"{entry_name}.json")
        
        # Write the entry as a standalone JSON file
        with open(output_file_path, "w") as output_file:
            json.dump(entry, output_file, indent=4)
        
        print(f"Extracted: {output_file_path}")

print("Data extraction complete.")
