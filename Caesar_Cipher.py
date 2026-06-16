# --- Caesar Cipher ---

def caesar_cipher(message, shift, mode):
    
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in message:
        
        if char.isalpha():
            # if char.isupper():
            #     new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # else:
            #     new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            result += new_char
            
        else:
            result += char

    return result