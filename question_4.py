import hashlib
import requests

def check_password_pwned(password):
    # Hash the password using SHA-1 as required by the "Have I Been Pwned" API
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Get the first 5 characters of the hash (prefix)
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    
    # Make a request to the "Have I Been Pwned" API with the hash prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from API: {response.status_code}")
    
    # Check if the hash suffix exists in the response data
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    file_path = "password_file.txt"
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                count = check_password_pwned(password)
                if count:
                    print(f"WARNING: The password for user '{username}' has been pwned {count} times!")
                else:
                    print(f"The password for user '{username}' is safe (not found in any breaches).")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()