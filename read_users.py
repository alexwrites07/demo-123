import json
import os

# Define input and output paths
input_path = os.path.join("c", "d", "users.json")
output_path = "extracted_users.json"

def extract_users():
    try:
        with open(input_path, "r") as f:
            data = json.load(f)
        users = data.get("users", [])

        with open(output_path, "w") as f:
            json.dump(users, f, indent=2)

        print(f"Extracted {len(users)} users to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_users()
