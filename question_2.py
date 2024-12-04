def rail_fence_encrypt(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    
    return "".join(result)

def rail_fence_decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
    
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
    
    return "".join(result)

def main():
    print("Rail Fence Cipher: Encryption and Decryption")
    
    choice = input("Choose an option (encrypt/decrypt): ").lower()
    text = input("Enter the text: ")
    key = int(input("Enter the key value: "))
    
    if choice == "encrypt":
        encrypted_text = rail_fence_encrypt(text, key)
        print("Encrypted text:", encrypted_text)
    elif choice == "decrypt":
        decrypted_text = rail_fence_decrypt(text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
