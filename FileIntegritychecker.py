import hashlib
import argparse
import os

def compute_hash(file_path, algorithm='sha256'):
    """Compute hash value of the file."""
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def save_hash(file_path, hash_value):
    """Save the hash to a .hash file."""
    with open(file_path + '.hash', 'w') as f:
        f.write(hash_value)

def load_hash(file_path):
    """Load the saved hash value."""
    try:
        with open(file_path + '.hash', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def verify_file(file_path, algorithm='sha256'):
    """Compare current hash with saved hash."""
    current_hash = compute_hash(file_path, algorithm)
    saved_hash = load_hash(file_path)

    if saved_hash is None:
        print(f"No hash found. Run without '--verify' to create one.")
        return

    if current_hash == saved_hash:
        print("✅ File integrity verified. No changes detected.")
    else:
        print("❌ File has been modified or corrupted!")
        print(f"Expected: {saved_hash}")
        print(f"Current:  {current_hash}")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("file", help="File to check")
    parser.add_argument("--verify", action="store_true", help="Verify file integrity")
    parser.add_argument("--algorithm", default="sha256", help="Hash algorithm (default: sha256)")

    args = parser.parse_args()

    if args.verify:
        verify_file(args.file, args.algorithm)
    else:
        hash_val = compute_hash(args.file, args.algorithm)
        save_hash(args.file, hash_val)
        print(f"{args.algorithm.upper()} hash saved: {hash_val}")

if __name__ == "__main__":
    main()
