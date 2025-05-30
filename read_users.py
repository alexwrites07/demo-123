import json

def extract_and_save_users(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
            users = data.get("users", [])

        with open(output_file, 'w') as f:
            json.dump(users, f, indent=2)
        print(f"'users' data saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_and_save_users("data.json", "users.json")
