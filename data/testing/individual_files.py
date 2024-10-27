import json
import os

# Define the names of the scenarios to extract
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

# Load the main JSON file
with open('../main_data.json', 'r') as file:
    data = json.load(file)

# Create individual files for each selected scenario
for scenario in data:
    scenario_name = scenario.get("name")
    if scenario_name in selected_names:
        # Define the filename based on the scenario name
        filename = f"{scenario_name}.json"
        
        # Write the individual scenario data to a new file
        with open(filename, 'w') as outfile:
            # Write scenario data as a single-element list for consistency with the structure
            json.dump([scenario], outfile, indent=4)
        
        print(f"Created file: {filename}")

print("Extraction completed.")
