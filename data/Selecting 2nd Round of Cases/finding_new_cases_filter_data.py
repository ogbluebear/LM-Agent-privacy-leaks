import json

def filter_data(input_file, output_file, selected_names):
    # Open and load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Filter the data by the selected entries
    filtered_data = [entry for entry in data if entry['name'] in selected_names]
    
    # Save the filtered data to the output file
    with open(output_file, 'w') as f:
        json.dump(filtered_data, f, indent=4)

# Specify your file paths
input_file = 'main_data.json'
output_file = 'inprog_filtered_output.json'

# Specify the list of selected entries
selected_names = [
    'main329', 'main336', 'main341', 'main345', 'main347', 'main358', 
    'main361', 'main362', 'main366', 'main371', 'main373', 'main377', 
    'main380', 'main381', 'main388', 'main392', 'main395', 'main398', 
    'main410', 'main411', 'main416', 'main421', 'main423', 'main426', 
    'main430', 'main444', 'main453', 'main462', 'main468', 'main472', 
    'main476', 'main480', 'main484', 'main492'
]


# Run the function
filter_data(input_file, output_file, selected_names)

print(f'Filtered data saved to {output_file}')
