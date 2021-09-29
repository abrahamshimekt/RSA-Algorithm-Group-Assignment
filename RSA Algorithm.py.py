"""
This is an RSA algorithm to encrypt
 a message by using modular a arithmetic
 """
import random

print("Hello Welcome to RSA Encryption Algorithm")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

"""
A function to check the inputs
 by the user if they are primes
 """


def is_prime(number):
    factor = 0
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                factor += 1
        if factor == 0:
            return True
        else:
            return False


def generate_prime():
    p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    if is_prime(p) and is_prime(q):
        return p, q
     
    else:
        while True:
            p = random.randint(100, 1000)
            q = random.randint(100, 1000)
            if is_prime(p) and is_prime(q):
                return p, q


rsa_tuple = generate_prime()
rsa_modulus = rsa_tuple[0] * rsa_tuple[1]
oiler = (rsa_tuple[0] - 1) * (rsa_tuple[1] - 1)


"""
This function returns the greatest common factor 
of two numbers by using Euclidean algorithm
"""


def gcd(num1, num2):
    if num2 == 0:
        return num1
    elif num2 == 1:
        return 1
    else:
        return gcd(num2, num1 % num2)


e = random.randint(100, 1000)

"""
This function generates a public key for encryption
"""


def generate_public_key(e):
    if gcd(e, oiler) != 1:
        while True:
            e = random.randint(100, 1000)
            if gcd(e, oiler) == 1:
                return e
    else:
        return e

e = generate_public_key(e)

"""
This function generate a private key
"""

def inverse():
    for d in range(1, oiler):
        if (d * e % oiler) == 1 % oiler:
            return d


print("public key:", (generate_public_key(e), rsa_modulus))
print("private key:", (inverse(), rsa_modulus))
message = input("enter the message to be encrypted:")
public_key = eval(input("please enter your public key to encrypt your message separated by comma:"))

"""
This function encrypts a message by using the ascii value
"""

def encrypt_message():
    global public_key
    message_list = []
    encrypted_list = []
    for character in message:             # convert each character to a number by their ascii value and add to a list
        message_list.append(ord(character))
    for item in message_list:              # encrypt each item of the list
        if public_key == (generate_public_key(e), rsa_modulus):
            encrypted_list.append(pow(item, public_key[0]) % public_key[1])      # m* =rem(pow(m,e),n) where m* is decrypted
        
        # message,m is original message,n is p*q
        else:
            public_key = eval(input("oops invalid key>>>plz try again!:"))
            encrypt_message()
    return encrypted_list


encrypted_message = "".join(str(item) for item in encrypt_message())
print("your encrypted message is:", encrypted_message)
secret_key = tuple(eval(input("enter your secret key to decrypt the message separated by comma:")))

"""
This function decrypt a message to its original meaning
"""

def decrypt_message():
    global secret_key
    decrypted_list = []
    for item in encrypt_message():
        if secret_key ==(inverse(),rsa_modulus):
            decrypted_list.append(pow(item, secret_key[0]) % secret_key[1])      # m= rem(pow(m*,d),n) where m is original
        
        # message m* is decrypted message and n is p*q
        else:
            secret_key= eval(input("oops invalid key>>>please try again!:"))
            decrypt_message()
    for i in range(len(decrypted_list)):
        decrypted_list[i] = chr(decrypted_list[i])
    return "".join(str(item) for item in decrypted_list)


print("your decrypted message is:", decrypt_message())
