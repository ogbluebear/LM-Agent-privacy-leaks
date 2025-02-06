import os
import json
import argparse

def process_outputs(folder_path):
    """
    Process JSON files in the specified folder to check for 'leak_info' and rename files accordingly.
    :param folder_path: Path to the folder containing output JSON files.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} does not exist.")
        return

    for file_name in os.listdir(folder_path):
        if not file_name.endswith(".json"):
            continue

        file_path = os.path.join(folder_path, file_name)

        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

            # Extracting the key (e.g., "main91") from the JSON structure
            scenario_key = list(data.keys())[0]
            leak_info = data[scenario_key].get("leak_info", False)

            # Process secret_judgment if leak_info is true
            if leak_info:
                secret_judgment = data[scenario_key].get("secret_judgment", [])
                judgment_sequence = "".join(["T" if judgment[1] else "F" for judgment in secret_judgment])

                # Rename the file
                new_file_name = f"true_{file_name.rsplit('.', 1)[0]}_{judgment_sequence}.json"
                new_file_path = os.path.join(folder_path, new_file_name)
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_name} -> {new_file_name}")
            else:
                print(f"No leak detected in: {file_name}")

        except json.JSONDecodeError:
            print(f"Error decoding JSON file: {file_name}")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Check for leaks in output JSON files and rename them accordingly.")
    parser.add_argument("-file", required=True, help="Name of the output scenario folder (e.g., 'outputs_main91')")
    args = parser.parse_args()

    # Process the folder
    folder_to_process = os.path.join(os.getcwd(), args.file)
    process_outputs(folder_to_process)
