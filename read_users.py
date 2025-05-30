import json

def print_users_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            users = data.get("users", [])
            print("Users:")
            for user in users:
                print(user)
    except Exception as e:
        print(f"Failed to read or parse {filename}: {e}")

if __name__ == "__main__":
    print_users_from_file("data.json")
