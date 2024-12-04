import random

def generate_password(dictionary_file_path, word_count=4):
    try:
        with open(dictionary_file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
            
        if len(words) < word_count:
            raise ValueError("The dictionary file doesn't contain enough words.")
        
        password_words = random.sample(words, word_count)
        password = ''.join(password_words)
        return password
    except FileNotFoundError:
        print("Error: The specified dictionary file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    dictionary_file_path = "dictionary.txt"
    password = generate_password(dictionary_file_path)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
