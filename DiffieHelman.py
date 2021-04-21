import random as rn
import math


class DH_Endpoint:
    def __init__(self, publicKey1, publicKey2, privateKey):
        self.privateKey = privateKey
        self.publicKey1 = publicKey1
        self.publicKey2 = publicKey2
        self.entireKey = None

    # function which we use to encrypt the keys
    def halfKey(self):
        halfKey = pow(self.publicKey1, self.privateKey)
        halfKey = halfKey % self.publicKey2
        return halfKey

    # the Key after combining and encrypting.
    def combinedKey(self, halfKey):
        combinedKey = pow(halfKey, self.privateKey)
        combinedKey = combinedKey % self.publicKey2
        self.entireKey = combinedKey
        return combinedKey

    # the encryption of the data
    def encrypt(self, data):
        ecryptedData = ""
        key = self.entireKey
        for c in data:
            ecryptedData += chr(ord(c) + (key % 1024))
        return ecryptedData

    # the decryption of the data
    def decrypt(self, data):
        decryptedData = ""
        key = self.entireKey
        for c in data:
            decryptedData += chr(ord(c) - (key % 1024))
        return decryptedData


# initialize of the Diffie-Helman Protocol.
# the order of the initialization is very important.
def DH_start(myPublicKey, recvPublicKey):
    if myPublicKey > recvPublicKey:
        return DH_Endpoint(myPublicKey, recvPublicKey, randomPrivateKey())
    elif recvPublicKey > myPublicKey:
        return DH_Endpoint(recvPublicKey, myPublicKey, randomPrivateKey())


# Generating the Private key.
def randomPrivateKey():
    return rn.randint(10, 50)


# Generating the public key using the functions below.
# Very high prime number
def RandomPNG():
    while True:
        value = rn.randint(100, 500)
        if primeCheck(value):
            value = Mersenne_number(value)
            return value


# Mersenne numbers are big prime numbers.
def Mersenne_number(prime):
    return pow(2, prime) - 1


# checking if a number is prime.
def primeCheck(prime):
    for i in range(2, int(math.sqrt(prime)) + 1):
        if (prime % i) == 0:
            return False
    return True

