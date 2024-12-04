
def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():  # Only process alphabetic characters
            shift_amount = shift % 26 
            if char.islower():  # Shift lowercase letters
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():  # Shift uppercase letters
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char  # Keep non-alphabetic characters unchanged
            
    return result

def caesar_cipher_decrypt(text, shift):
    # Decryption is simply encryption with a negative shift
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher: Encryption and Decryption")
    
    choice = input("Choose an option (encrypt/decrypt): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == "encrypt":
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == "decrypt":
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
