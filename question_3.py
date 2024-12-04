import hashlib

def hash_password_sha256(password):
    # Create a sha256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the password encoded to bytes
    sha256.update(password.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return sha256.hexdigest()

def main():
    password = input("Enter the password: ")
    hashed_password = hash_password_sha256(password)
    print("SHA-256 Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()
