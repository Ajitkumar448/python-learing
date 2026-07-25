def caesar(text,shift,encrypt=True):# to define the caesar function that takes in the text, shift and encrypt parameters
    if not isinstance(shift,int):# to check the type of shift
        raise TypeError("Shift must be an integer") #   to check the type of shift
    if shift<1 or shift>25:# to check the range of shift
        raise ValueError("Shift must be between 1 and 25")# to check the range of shift
    alphabet = "abcdefghijklmnopqrstuvwxyz"# to define the alphabet
    if not encrypt:# to check if the user wants to encrypt or decrypt
        shift = -shift # to shift the alphabet in the opposite direction for decryption
    shift_alphabet = alphabet[shift:]+alphabet[:shift]# to shift the alphabet
    transtable = str.maketrans(alphabet +alphabet.upper(),shift_alphabet +shift_alphabet.upper()) # to create a translation table
    encrypted_text = text.translate(transtable) # to translate the text using the translation table 
    return encrypted_text # to return the encrypted text
def encrypt(text,shift):
    return caesar(text,shift,encrypt=True) # to encrypt the text using the caesar function
def decrypt(text,shift):
    return caesar(text,shift,encrypt=False) # to decrypt the text using the caesar function

encrypted_text = encrypt("Hello World", 3) # to encrypt the text with a shift of 3
decrypted_text = decrypt(encrypted_text, 3) # to decrypt the encrypted text with a shift of 3
print(encrypted_text) # to print the encrypted text
print(decrypted_text) # to print the decrypted text


