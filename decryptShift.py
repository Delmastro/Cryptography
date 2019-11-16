
def decrypt_shift_cipher():

    alpha = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = input("Enter the encrpyted text: ").lower()
    decrypted_list = []

    for shift_key in range(0,26):
        plaintext = ""
        for letter in ciphertext:
            plaintext += alpha[(alpha.index(letter) + shift_key) % len(alpha)]
        decrypted_list.append(plaintext)
    [print(i, plain.upper()) for i, plain in enumerate(decrypted_list)]
    
decrypt_shift_cipher()

