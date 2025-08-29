File Integrity Checker

A simple Python tool to *monitor file changes* by calculating and comparing cryptographic hash values.  
This helps ensure files are not *modified, corrupted, or tampered with*.

COMPANY: CODETECH IT SOLUTIONS
NAME:Rahman Fayid PM
Intern ID:CTO4DZ2301
DOMAIN: Cyber Security And Ethical Hacking 
DURATION: 4 WEEKS 
MENTOR: NEELA SANTOSH

🖥 Usage
1. Save a file hash

Generate and store the hash of a file (default: SHA256):

python file_integrity_checker.py example.txt


This creates a .hash file (example.txt.hash) storing the computed hash.

2. Verify file integrity

Check if the file has been modified or corrupted:

python file_integrity_checker.py example.txt --verify


✅ Output if unchanged:

File integrity verified. No changes detected.


❌ Output if modified:

File has been modified or corrupted!
Expected: <saved_hash>
Current:  <new_hash>

3. Use a different hashing algorithm

You can specify algorithms supported by Python’s hashlib (e.g., md5, sha1, sha256, sha512):

python file_integrity_checker.py example.txt --algorithm sha512
