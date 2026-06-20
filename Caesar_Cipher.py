# =====================
# === Caesar Cipher ===
# =====================

def caesar_cipher(text, shift, mode):
    
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            result += new_char
            
        else:
            result += char

    return result

# _________________________________________________________________________________________________

print("=== Caeser Cipher ===")

while True:
    choice = input("Encrypt or Decrypt? (e/d):").lower()

    if choice in ["e", "d"]:
        break

    print("Enter 'e' or 'd' only")

message = input("Enter your encrypted message:")

while True:
    try:
        shift = int(input("Enter shift value:"))
        break
    except ValueError:
        print("Enter a number")

if choice == "e" :
    output = caesar_cipher(message, shift, "encrypt")
    print("\nEncrypted message:")

else:
    output = caesar_cipher(message, shift, "decrypt")
    print("\nDecrypted message:")

print(output)

# _________________________________________________________________________________________________