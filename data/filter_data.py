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
output_file = 'original_filtered_output.json'

# Specify the list of selected entries
selected_names = [
    'main91', 'main92', 'main95', 'main97', 'main98', 'main105', 'main113', 'main115', 'main119', 
    'main121', 'main127', 'main141', 'main143', 'main154', 'main162', 'main168', 'main173', 'main176', 'main187', 
    'main191', 'main196', 'main200', 'main204', 'main231', 'main242', 'main263', 'main266', 'main275', 
    'main277', 'main278', 'main280', 'main281', 'main283', 'main290', 'main300', 'main302', 'main304', 'main305', 
    'main309'
]

# Run the function
filter_data(input_file, output_file, selected_names)

print(f'Filtered data saved to {output_file}')
