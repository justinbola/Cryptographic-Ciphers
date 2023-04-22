# Cryptographic Ciphers
# Author: Justin Bola
# Description: Vigenere and Affine cipher IOCs, plus histogram and decryption

# Source consulted:
# https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-IOC.html
# This uses the vigenere cipher (Cipher: A)
ciphertextVigenere = 'fvzhpwsggfcpzxwzmbtthjnwdhyxzxbwdszhusnmdbzcnfuuwmfjaeewfvvqsyyhuzcioimlafptuhmqainpriohubpdbv' \
                     'vwpoesiifaqjvloenwhsinvyqszhkdiifaqjvnvynswskwlvyvbwcafsokfopxuaifpsiahrxszrzhosqqaiyddhywbhyt' \
                     'yevtuhydsiagqgittigtqfrasmggrtvgpraaehytavoltbfiomhyycit'
# Convert ciphertext to uppercase for easy access and modification
upperVigenere = ciphertextVigenere.upper()
# This uses the affine cipher (Cipher: B)
ciphertextAffine = 'oyvrvrzdlumtronytgnhteohuoyvroyhuhvrgdolugvgbqtnpzdlotphoyhqmlhavmmoyhroduzhgkrzdlftphlavgzdluqh' \
                   'ktgkqhmvhihfytohihuzdlftgoodqhmvhihzdlotphoyhuhkavmmzdlrotzvgfdgkhumtgktgkvrydfzdlydfkhhaoyhutqq' \
                   'voydmhbdhruhjhjqhutmmvjdeehuvgbvroyhouloygdoyvgbjduh'
# Convert ciphertext to uppercase for easy access and modification
upperAffine = ciphertextAffine.upper()


# Function to calculate the IOC of ciphertexts
def calc_ic(cipher):
    # Store each letter in the ciphertext to new variable called cipher
    cipher = ''.join([letter for letter in cipher])
    # Note: Multiply array by 26 since we are dealing with the English language
    letters = 26 * [0]
    # Set n equal to the length of the ciphertext
    n = len(cipher)
    # Loop through the ciphertext
    for letter in cipher:
        # Increment the array index by one
        letters[ord(letter) - 65] = letters[ord(letter) - 65] + 1
    # Store information in a variable called index
    index = sum([entry * (entry - 1) for entry in letters])
    # Divide index of coincidence by length of ciphertext multiplied by itself subtracted by one
    index /= n * (n - 1)
    # Print the index of coincidence
    print(f'{index}')


# Sources consulted:
# https://statisticsbyjim.com/basics/histograms/
# https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

# Function to print the histogram
def print_histogram(cipher):
    # Store frequency in a dictionary
    frequency = {}
    # Loop through the ciphertext
    for index in cipher:
        # If the letter is already registered in the frequency dictionary
        if index in frequency:
            # Increment the frequency for specified letter
            frequency[index] = frequency[index] + 1
        # If the letter is not already registered in the frequency dictionary
        else:
            # Set the frequency of specified letter to one
            frequency[index] = 1
    # Print the histogram
    print(str(frequency))


# Source consulted:
# https://www.cs.uri.edu/cryptography/classicalaffine.htm

# Function to find modular inverse
def inverse(a, m):
    # Call extended euclidean algorithm function to set variables to find inverse
    gcd, x, y = euclidean(a, m)
    # Return modular inverse
    return x % m


# Function to calculate using extended euclidean algorithm (Relied on 2nd source [cited above] for exact calculations)
def euclidean(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    # Return greatest common divisor, x, y
    return gcd, x, y


# Function to decrypt the affine ciphertext
def decrypt_cipher(cipher, key):
    # Return and format the decrypted affine cipher
    return ''.join([chr(((inverse(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])


# Call functions in order to calculate IC, print the histogram, and decrypt the affine cipher
print('Index of coincidence for Vigenere Cipher:')
calc_ic(upperVigenere)
print('Index of coincidence for Affine Cipher:')
calc_ic(upperAffine)
print('Histogram for Affine Cipher:')
print_histogram(ciphertextAffine)
# Set private key equal to result calculated via part C
private_key = [23, 19]
print('Decrypted affine cipher: {}'.format(decrypt_cipher(ciphertextAffine, private_key)))
