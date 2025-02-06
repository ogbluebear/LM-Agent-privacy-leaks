import os
import subprocess
import argparse

# Path to the evaluation script
EVALUATION_SCRIPT = r"D:\LM-Agent-privacy-leaks\evaluation\gpt_evaluate_action.py"

def fix_leaked_file_format(file_path):
    """
    Ensures the leaked JSON file has an opening bracket at the beginning
    and a closing bracket at the end to make it a valid JSON array.
    """
    with open(file_path, 'r') as file:
        content = file.read().strip()

    if not content.startswith("["):
        content = f"[{content}]"

    with open(file_path, 'w') as file:
        file.write(content)

def process_evaluation(input_dir):
    """
    Process the evaluations for a single scenario directory (e.g., evaluation_main91).
    :param input_dir: Path to the specific evaluation folder (e.g., evaluation_main91).
    """
    # Ensure the provided directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Directory {input_dir} does not exist.")
        return

    # Iterate through all subfolders (e.g., evaluation_main91_test1, evaluation_main91_test2)
    for subfolder in os.listdir(input_dir):
        subfolder_path = os.path.join(input_dir, subfolder)

        # Ensure this is a valid directory
        if not os.path.isdir(subfolder_path):
            continue

        # Check for the CSV file in the subfolder
        csv_file = next((f for f in os.listdir(subfolder_path) if f.endswith(".csv")), None)
        if not csv_file:
            print(f"Skipping {subfolder_path}, no CSV file found.")
            continue

        csv_path = os.path.join(subfolder_path, csv_file)

        # Extract folder base name and test number for locating the leaked JSON
        folder_base_name = os.path.basename(input_dir).split("_")[1]  # Extract "main91" from "evaluation_main91"
        test_number = subfolder.split("_")[-1].replace("test", "")  # Extract "1" from "evaluation_main91_test1"

        # Locate the leaked JSON file in the parent folder
        parent_folder = input_dir
        leaked_json_name = f"Leaked_{folder_base_name}_test{test_number}_try"
        leaked_json_path = None

        # Search for the leaked JSON file with the correct prefix
        for file in os.listdir(parent_folder):
            if file.startswith(leaked_json_name) and file.endswith(".json"):
                leaked_json_path = os.path.join(parent_folder, file)
                break

        if not leaked_json_path:
            print(f"Leaked JSON file not found for {csv_file} in {parent_folder}")
            continue

        # Fix the leaked JSON file format
        fix_leaked_file_format(leaked_json_path)

        # Set the output path for the evaluation results
        eval_output_name = f"EvalOutput_{folder_base_name}_test{test_number}.json"
        eval_output_path = os.path.join(
            r"D:\LM-Agent-privacy-leaks\data\testing\gpt-4o-mini-results", eval_output_name
        )

        # Run the evaluation script
        try:
            print(f"Processing: {csv_path} with Leaked JSON: {leaked_json_path}")
            subprocess.run([
                "python", EVALUATION_SCRIPT,
                "--data-path", leaked_json_path,
                "--action-path", csv_path,
                "--step", "judge_leakage",
                "--output-path", eval_output_path
            ], check=True)
            print(f"Completed: {eval_output_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {csv_path}: {e}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Evaluate different models on a specific scenario folder.")
    parser.add_argument("-file", required=True, help="Path to the specific evaluation directory (e.g., evaluation_main91)")
    args = parser.parse_args()

    # Process the provided directory
    process_evaluation(args.file)
