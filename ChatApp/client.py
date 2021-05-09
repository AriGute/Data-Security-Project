import socket, threading
import ChatApp.DiffieHelman as dh

class Client():

    def __init__(self):
        self.cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_receive = threading.Thread(target=self.receive)
        self.SendMessagFunc = ""
        self.forceQuit = ""

        # Diffie Helman private & public keys initialize
        self.prvKey = dh.randomPrivateKey()
        self.pubKey = None
        self.DH = None


    def BindMessageFunction(self, messageFunc, forceQuit):
        # Bind the function that send message to the other side.
        self.SendMessagFunc = messageFunc;
        self.forceQuit = forceQuit

    def StartClient(self, name='name', password="password", HOST='localhost', PORT=5023):
        print("StartClient start")
        self.cli_sock.connect((HOST, PORT))
        self.SendMessagFunc('Connected to remote host...')
        self.myName = name
        self.myPass = password
        self.firstToSend = False
        uname = (name+" /authRequest").encode("UTF-8").strip()
        print(uname)
        self.cli_sock.send(uname)
        self.thread_receive.start()
        print("StartClient Done.")

    def send(self, msg):
        print("send["+msg+"]")
        if self.myToken is not None:
            if self.SendMessagFunc == '':
                print("Message function must be binding first.")
            else:
                if self.DH is not None:
                    if self.DH.entireKey is not None:
                        self.SendMessagFunc(self.myName + ": " + msg)
                        msg = self.DH.encrypt(msg + " ")
                        print("ENC MSG -> send[" + msg + "]")
        splitSign = "|ยง|"
        msg += splitSign + self.myToken
        self.cli_sock.send(msg.encode("UTF-8").strip())

    def receive(self):
        while True:
            print("Start receive loop\n")
            # sen_name = self.cli_sock.recv(1024).decode("UTF-8").strip()
            data = self.cli_sock.recv(4096).decode("UTF-8").strip()
            print("befor DEC MSG -> recv[" + data + "]")
            if "/" in str(data) and self.DH is None:
                print("Start ChatCommand")
                self.ChatCommand(data)
            elif "/" in str(data):
                print("Start ChatCommand")
                self.ChatCommand(data)
            elif self.DH is not None:
                if self.DH.entireKey is not None:
                    print("first receive if")
                    if self.SendMessagFunc == '':
                        print("Message function must be binding first.")
                    else:
                        # self.SendMessagFunc("Decrypting message with key: " +  str(self.DH.entireKey))
                        temp = data.split(':')
                        msg = self.DH.decrypt(temp[1])
                        print("Message decrypted..")
                        # self.SendMessagFunc(sen_name + ": " + str(data))
                        self.SendMessagFunc(str(temp[0]) + ": " + str(msg))
                        print("DEC MSG -> recv[" + data + "]")
            else:
                print("second receive if")
                if self.SendMessagFunc == '':
                    print("Message function must be binding first.")
                else:
                    self.SendMessagFunc("Error: No key to decipher")

    # Simple encryption -> Caesar cipher
    def Encryption(self, user):
        print(user)
        username = user[0]
        password = user[1]
        sum = 0  # The sum of each letter in password => to create a number and use caesar cipher
        encrypted_pass = ""
        for i in username:
            sum += ord(i)

        for c in str(password):
            encrypted_pass += chr((ord(c) + sum))
        encrypted_pass += chr(sum)
        return encrypted_pass

    # Simple decryption -> Caesar cipher
    def Decryption(self, key, encrypted_pass):
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
            # print("char after: " + decrypted_pass)

        print("decription after: " + decrypted_pass)

        return decrypted_pass

    def DHsendPubKey(self):
        print("SendPubKey start")
        self.pubKey = dh.RandomPNG()
        self.send(msg="/key "+str(self.pubKey))
        print("SendPubKey end\n")

    def DHinit(self, data):
        print("DHinit start")
        self.DH = dh.DH_start(self.pubKey, data.split(' ')[1])
        print("DHinit next 1")
        halfKey = self.DH.halfKey()
        print("DHinit next 2")
        print("helf key: "+str(halfKey))
        self.send(msg="/halfKey " + str(halfKey))
        print("DHinit end\n")

    def SaveToken(self, data):
        print("SaveToken start")
        print("beforE: " + str(data))
        self.myToken = self.Decryption(self.myPass , data.split(' ')[1])
        print("after: "+str(self.myToken))

    def ChatCommand(self, data):
        #~~~~~~~~~~~~~~Authentication Session~~~~~~~~~~~~~~
        if "/auth" in str(data):
            self.send(self.myName)

        elif "/token" in str(data):
            self.SaveToken(data)

        elif "/unAuth" in str(data):
            print("Unauthorized use.\n[FORCE QUITE]\n")
            self.forceQuit()
            exit()
        #~~~~~~~~~~~~~~Authentication Session~~~~~~~~~~~~~~

        #~~~~~~~~~~~~~~Diffie Helman Session~~~~~~~~~~~~~~
        elif "/send" in str(data):
            print("send command")
            if self.pubKey is None:
                print("send func")
                self.firstToSend = True
                self.DHsendPubKey()

        elif "/key" in str(data):
            print("key command")
            if self.firstToSend is False:
                self.DHsendPubKey()
            else:
                self.DHinit(data)
                self.DH.combinedKey(data.split(' ')[1])

        elif "/halfKey" in str(data):
            print("helfkey command")
            if self.firstToSend is False:
                self.DHinit(data)
            self.DH.combinedKey(data.split(' ')[1])
        #~~~~~~~~~~~~~~Diffie Helman Session~~~~~~~~~~~~~~

        else:
            print("Unrecognized command")
