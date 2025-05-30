import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def print_users(data):
    if "users" in data:
        for user in data["users"]:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    else:
        print("No 'users' key found in JSON data.")

if __name__ == "__main__":
    file_name = "data.json"
    json_data = read_json_file(file_name)
    if json_data:
        print_users(json_data)
