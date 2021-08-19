
# COMP596 - Cryptography
# Homework 2  -
# Brenner Campos
#import cipher as cipher


def RC4_Init (secret_key, plaintext):

    S = list(range(256))
    K = list(range(256))
    PT = list()

    # Converting each character in our plaintext to decimal, and then to binary format
    for i in range(len(plaintext)):
        decimal = ord(plaintext[i])
        pt_binary = f'{decimal:08b}'
        PT.append(pt_binary)

    print("PT IN BINARY: ", PT)

    # Doing our permutations
    for i in range(256):
        S[i] = i
        K[i] = K[i % len(secret_key)]
    j = 0
    for i in range(256):
        j = (j + S[i] + K[i % len(secret_key)]) % 256
        S[i], S[j] = S[j], S[i] # Swap-aroonie

    print("S: ", S)

    return S, PT


def RC4_Keystream(S, binary):


    # our Ciphertext holding list
    C = list()
    bytes_left = secret_key_length

    i = j = 0

    # While there are more bytes to encrypt...
    while (bytes_left > 0):

        # Doing our 'magic'
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        # Swapping S[i] with S[j]
        S[i], S[j] = S[j], S[i]

        # Getting our index, t
        t = (S[i] + S[j]) % 256

        # Uses S[t] as keystream byte, and converts it to 8 bit binary format
        keystream_byte = f'{S[t]:08b}'
        # print(keystream_byte)


        # XORing the binaries of the plaintext with our generated keystream_byte binary
        C.append(int(binary[i],2) ^ int(keystream_byte,2))

        # test = (int(binary[i],2) ^ int(keystream_byte,2))
        # print("TEST:" , test)
        #
        # for i in range(len(test)):
        #     bin = f'{test[i]:08b}'
        #     Tst.append(bin)
        #
        # print(Tst)

        bytes_left -= 1

    return C


def encryption_RC4(S, pt_binary):

    S_binary = list()

    # Converting decimals in S into binary and adding to a new list
    for i in range(len(S)):
        bin = f'{S[i]:08b}'
        S_binary.append(bin)
    print("S IN BINARY: ", S_binary)

    # Calling Keystream generator with S and our plaintext binary list
    C = RC4_Keystream(S, pt_binary)

    print("C: ", C)

    cipher_text = ''

    # building a ciphertext by converting new C list
    for i in range(len(C)):
        cipher_text += chr(C[i])

    print("RESULTING CIPHERTEXT: ", cipher_text)

    return cipher_text, S_binary




def decryption_RC4(S, CT, S_binary):


    plaintext = list()
    C_binary = list()


    # plain_text = ''
    # for i in range(len(P)):
    #     plain_text += chr(P[i])


    # Converting from ASCII to decimal format
    for i in range(len(CT)):
        plaintext.append(str(ord(CT[i])))
    print("plaintext decimal: ", plaintext)



    P = RC4_Keystream(S, S_binary)
    print("P: ", P)
    # for i in range(len(P)):


    for i in range(len(P)):
        bin = f'{int(P[i]):08b}'
        C_binary.append(bin)
    print("C IN BINARY: ", C_binary)
    print("S_binary: ", S_binary)



    plain_text = ''

    for i in range(len(P)):
        plain_text += chr(P[i])

    print("RESULTING PLAINTEXT: ", plain_text)

    return plain_text




# --- -- -- START OF PROGRAM  -- -- -- - - -- -- - - --- - - -- - - --- ---- -- -

M = list()


# SECRET KEY AND PLAINTEXT #1
secret_key = "abracadabra"
secret_key.lower()
secret_key_length = len(secret_key)
plaintext = 'Never say never'
print("SECRET KEY:  " + secret_key + "  -  LENGTH: " + str(secret_key_length))
print("PLAINTEXT: ", plaintext)

# Calling initialization of RC4 with our key and message, getting S-table and plaintext binaries
S, pt_binary = RC4_Init(secret_key, plaintext)


# Using our obtained S-table and plaintext binaries to encrypt the message
CT, S_binary = encryption_RC4(S, pt_binary)




PT = decryption_RC4(S, CT, S_binary)





# print("RESULTING PLAINTEXT: ", plain_text)
# print(PT)






