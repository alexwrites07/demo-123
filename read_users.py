import json
import os

SRC_ROOT = "c"
DST_ROOT = "extracted_users"

def extract_and_preserve_structure():
    for dirpath, _, filenames in os.walk(SRC_ROOT):
        for filename in filenames:
            if filename.endswith(".json"):
                src_file_path = os.path.join(dirpath, filename)
                # Compute relative path from SRC_ROOT
                rel_path = os.path.relpath(src_file_path, SRC_ROOT)
                dst_file_path = os.path.join(DST_ROOT, rel_path)

                os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)

                try:
                    with open(src_file_path, "r") as f:
                        data = json.load(f)

                    users = data.get("users", [])

                    # Save only users array to new file preserving structure
                    with open(dst_file_path, "w") as f:
                        json.dump({"users": users}, f, indent=2)

                    print(f"Processed {src_file_path} → {dst_file_path}")

                except Exception as e:
                    print(f"Failed to process {src_file_path}: {e}")

if __name__ == "__main__":
    extract_and_preserve_structure()
