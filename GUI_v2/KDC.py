## Implemenation of encryption and decryption of Kerberos Data base
## Kerberos functions goes here

import random

class Kdc:

    def __init__(self, dbPath=""):
        self.dbPath  = dbPath

    # Simple encryption -> Caesar cipher
    def Encryption(self, set):
        print("kdc encrypt: " + str(set))
        key = set[0]
        msg = set[1]
        sum = 0  # The sum of each letter in password => to create a number and use caesar cipher
        encrypted_pass = ""
        for i in key:
            sum += ord(i)
        print(sum)
        # print(sum%32)

        for c in str(msg):
            encrypted_pass += chr((ord(c) + sum))
        # encrypted_pass += chr(sum)
        return encrypted_pass

    # Simple decryption -> Caesar cipher
    def Decryption(self,key ,encrypted_pass):
        # encrypted_pass.strip(str(ord()))
        print("decription input: " + encrypted_pass)
        print("key input: " + key)

        encrypted_pass = encrypted_pass.rstrip('\x00')
        encrypted_pass = encrypted_pass.rstrip('\n')

        decrypted_pass = ""

        sum = 0  # The sum of each letter in password => to create a number and use caesar cipher
        for i in key:
            sum += ord(i)
        print("sum: " + str(sum))
        # print("kdc decrypt: "+key)
        for c in encrypted_pass:
            # print("char befor: " + c)
            decrypted_pass += chr((ord(c) - sum))
            # print("char after: "+decrypted_pass)

        print("decription after: " + decrypted_pass)
        return decrypted_pass

    def AddUser(self, user):
        encryptedPassword = str(self.Encryption(user))
        ascii = user[0].encode("utf-8")+":".encode("utf-8")+encryptedPassword.encode("utf-8")+"\n".encode("utf-8")

        dbFile = open(self.dbPath + "DB.txt", "ab")
        dbFile.write(ascii)
        dbFile.close()

    def GetUser(self, userName):
        user = self.Login(userName)
        user = (user.split(":")[0],user.split(":")[1].replace("\n",""))
        userPass = self.Decryption(user[0], user[1])
        print("getUser: "+userPass)
        return userPass

    def experemential(self):
        user = "ariel"
        password = self.Login(user)
        print("password: " + password)
        decPass = self.Decryption(user, password.split(":")[1])
        print(decPass)


    def Login(self, uname):
        username = uname[0]
        for line in open("DB.txt", "rb").readlines():  # Read the lines
            login_info = line.decode("utf-8")
            print("login: "+username)
            if username in login_info:
                # print("login: "+login_info)
                # login_info.replace("\n", "")
                return login_info
        print("Incorrect credentials.")
        return False

