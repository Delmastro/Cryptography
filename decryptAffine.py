def decrypt_affine(a, b, ciphertext): 

     """Function which will decrypt an affine cipher.

   Parameters:
         a (int): A random integer given by "a" between 0 and the length of the alphabet
         b (int) : A random integer given by "b" between 0 and the length of the alphabet
         ciphertext (str): The given cipher which we want to decrypt.

     Return:
         decrypted_string (str): If the inverse exists, then a string with be.""" 

     decrypted_string = ""

#     inverse = find_inverse(a, len(alpha))

#     if inverse == None:
#         return None

#     for character in ciphertext:
#         decrypted_character = (inverse*(char_to_int(character) - b)) % len(alpha)
       
#         decrypted_string += (int_to_char(decrypted_character))

#     return decrypted_string
    

# def int_to_char(i):

#     return alpha[i] 


# def char_to_int(c):

#     return alpha.index(c)
