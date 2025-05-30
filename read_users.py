import json
import os

def extract_all_users(root_folder="c"):
    combined_users = []

    # Walk through all files recursively inside 'c'
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".json"):
                file_path = os.path.join(dirpath, filename)
                print(f"Processing: {file_path}")
                try:
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    users = data.get("users", [])
                    if isinstance(users, list):
                        combined_users.extend(users)
                    else:
                        print(f"Warning: 'users' key in {file_path} is not a list")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

    # Save combined users to a new file
    with open("combined_users.json", "w") as f:
        json.dump(combined_users, f, indent=2)

    print(f"✅ Extracted total {len(combined_users)} users from all JSON files.")

if __name__ == "__main__":
    extract_all_users()
