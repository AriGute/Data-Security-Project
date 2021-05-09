import random as rn
import math
from numpy import double


class DH_Endpoint:
    def __init__(self, publicKey1, publicKey2, privateKey):
        self.privateKey = privateKey
        self.publicKey1 = publicKey1
        self.publicKey2 = publicKey2
        self.entireKey = None

    # function which we use to encrypt the keys
    def halfKey(self):
        print("pubKey1 = " + str(self.publicKey1))
        print("pubKey2 = " + str(self.publicKey2))
        halfKey = pow(self.publicKey1, self.privateKey)

        print("halfKey(BEFORE MODULO) : " + str(halfKey))
        # halfKey = halfKey % self.publicKey2
        halfKey = self.publicKey2 % halfKey

        print("halfKey(AFTER MODULO) : " + str(halfKey))
        return halfKey

    # the Key after combining and encrypting.
    def combinedKey(self, halfKey):
        print("helf key: "+str(halfKey)+"\nprivateKey: "+ str(self.privateKey))
        combinedKey = pow(int(halfKey), self.privateKey)
        print("combinedKey: " + str(combinedKey)+"\npublicKey2: "+str(self.publicKey2))
        combinedKey = self.publicKey2 % combinedKey

        # combinedKey = combinedKey % self.publicKey2

        print("combinedKey: " + str(combinedKey))
        print("publicKey2: " + str(self.publicKey2))

        print("entireKey raw : " + str(combinedKey % int(self.publicKey2)))
        print("entireKey: " + str(self.entireKey))
        self.entireKey = combinedKey
        print("entireKey: " + str(self.entireKey) +"\nprivet: "+ str(self.privateKey) +"\npublic1: "  + str(self.publicKey1) + "\npublic2: " +str(self.publicKey2)+"\n")
        return combinedKey

    # the encryption of the data
    def encrypt(self, data):
        ecryptedData = ""
        key = self.entireKey
        for c in data:
            ecryptedData += chr(ord(c) + (int(key) % 256))
        return ecryptedData

    # the decryption of the data
    def decrypt(self, data):
        decryptedData = ""
        key = self.entireKey
        for c in data:
            decryptedData += chr(ord(c) - (int(key) % 256))
        return decryptedData


# initialize of the Diffie-Helman Protocol.
# the order of the initialization is very important.
def DH_start(myPublicKey, recvPublicKey):
    recvPublicKey = int(recvPublicKey)
    print(type(recvPublicKey))

    if myPublicKey >= recvPublicKey:
        return DH_Endpoint(myPublicKey, recvPublicKey, randomPrivateKey())
    elif recvPublicKey > myPublicKey:
        return DH_Endpoint(recvPublicKey, myPublicKey, randomPrivateKey())
    else:
        print("Public keys are alike, no Initiation has occured")
        exit()

# Generating the Private key.
def randomPrivateKey():
    return rn.randint(3, 8)

# Generating the public key using the functions below.
# Very high prime number
def RandomPNG():
    value = rn.randint(1000, 10000)
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

# print("PrvKey = " + str(randomPrivateKey()) + " PubKey = " + str(RandomPNG()))
#
# pubKey1 = RandomPNG()
# pubKey2 = RandomPNG()
#
# dh1 = DH_start(pubKey1, pubKey2)
# halfKey1 = dh1.halfKey()
# print(halfKey1)
#
# dh2 = DH_start(pubKey2, pubKey1)
# halfKey2 = dh2.halfKey()
# print(halfKey2)
#
# dh1.entireKey = dh1.combinedKey(halfKey1)
# dh2.entireKey = dh2.combinedKey(halfKey2)
#
# print(dh1.entireKey)
# print(dh2.entireKey)
#
# a = dh1.encrypt("yoav a maniak")
# print("a: "+a)
# a = dh2.decrypt(a)
# print("a: "+a)
