import os
import subprocess
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Run iterative modifications and optimize all files.")
parser.add_argument("-file", required=True, help="Path to the input JSON file for optimization.")
args = parser.parse_args()

# Input file path
input_file_path = args.file

# Extract filename and directory information
base_dir = os.path.dirname(input_file_path)
filename = os.path.splitext(os.path.basename(input_file_path))[0]
evaluation_dir = os.path.join(base_dir, f"evaluation_{filename}")

# Path to iterative_modification.py in the evaluation folder
evaluation_folder = os.path.dirname(os.path.abspath(__file__))
iterative_modification_path = os.path.join(evaluation_folder, "iterative_modification.py")

# Step 1: Execute iterative_modification.py
if not os.path.exists(iterative_modification_path):
   raise FileNotFoundError(f"iterative_modification.py not found at {iterative_modification_path}")

#print(f"Running iterative modifications for file: {input_file_path}")
#subprocess.run(["python", iterative_modification_path, "-file", input_file_path], check=True)

# Step 2: Run optimize_single.py for each of the 10 generated files
for i in range(8, 11):
    modified_file = os.path.join(evaluation_dir, f"{filename}_test{i}.json")
    if not os.path.exists(modified_file):
        print(f"Modified file not found: {modified_file}. Skipping.")
        continue

    print(f"Running optimization on: {modified_file}")
    subprocess.run(["python", "optimize_single.py", "-file", modified_file], check=True)

print("All optimizations completed.")
