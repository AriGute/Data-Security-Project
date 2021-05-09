import socket, threading, time
import  random
import  GUI_v2.KDC

class Server(GUI_v2.KDC.Kdc):
    def __init__(self, path = ""):
        self.dbPath = path
        self.CONNECTION_LIST = []
        self.serverPassword = "password"

        self.authDict = {}

        self.ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_ac = threading.Thread(target=self.Accept_client)
        self.flag = 0;

    def StartServer(self):
        HOST = 'localhost'
        PORT = 5023
        self.ser_sock.bind((HOST, PORT))
        self.ser_sock.listen(1)
        print('Chat server started on port : ' + str(PORT))
        self.thread_ac.start()

    def GeneratePrivateNum(self):
        randNum = random.randint(100000000000,999999999999)
        return str(randNum)

    def Accept_client(self):
        while True:
            # accept
            cli_sock, cli_add = self.ser_sock.accept()

            uname = cli_sock.recv(4096)
            uname = uname.decode("utf-8")

            msg = uname.split(" ")[1]

            uname = uname.split(" ")[0]
            print("want auth: "+uname+", "+msg)


            if "/authRequest" in msg:
                if self.Login(uname) is not False:
                    print("create and send private token.")
                    self.authDict.update({uname: self.GeneratePrivateNum()})
                    token = self.authDict.get(uname)
                    token = self.Encryption((self.serverPassword, token))
                    print("send token 1: "+str(token))
                    privatePassword = self.GetUser((uname, ""))
                    token = self.Encryption((privatePassword, token))
                    print("send token 2: "+str(token))

                    msg = "/token" + " " + token
                    cli_sock.send(msg.encode("utf-8").strip())
                    print("token sent.")
                    uname = uname.encode("utf-8")
                    thread_client = threading.Thread(target=self.Broadcast_usr, args=[uname, cli_sock])
                    thread_client.start()

                    self.CONNECTION_LIST.append((uname, cli_sock))
                    print('%s is now connected' % uname.decode('UTF-8').strip())

                    if len(self.CONNECTION_LIST) + self.flag == 2:
                        self.flag = 1
                        time.sleep(1.5)
                        print("sending: " + self.CONNECTION_LIST[0][0].decode("UTF-8").strip())
                        self.B_usr(self.CONNECTION_LIST[1][1], self.CONNECTION_LIST[1][0],
                                   "/send".encode('UTF-8').strip())
                else:
                    msg = "/unAuth"+" None."
                    cli_sock.send(msg.encode("utf-8").strip())
                    print("Client is unauthorized.")




    def Broadcast_usr(self, uname, cli_sock):
        while True:
            data = cli_sock.recv(4096)
            if data:
                print("real message: "+data.decode("UTF-8"))
                splitSign = "|ยง|"
                userToken = data.decode("UTF-8").split(splitSign)[1]

                data = (data.decode("UTF-8").split(splitSign)[0]).encode("utf-8")
                print("B_U uToken: " + userToken)

                recvUserPrivatNum = self.Decryption(self.serverPassword, userToken)
                # recvUserPrivatNum = self.Decryption(self.GetUser(uname.decode("utf-8")), userToken).rstrip('\x00')
                # print("B_U recvPrivNum: " + recvUserPrivatNum)

                realUserPrivatNum = self.authDict.get(uname.decode("utf-8"))
                print("B_U realPrivNum: " + realUserPrivatNum)
                print("\n")
                if recvUserPrivatNum == realUserPrivatNum:
                    # print("data: "+data.decode('UTF-8').strip())
                    print("{0} spoke".format(uname.decode('UTF-8')))
                    self.B_usr(cli_sock, uname, data)
                else:
                    print("Message is missing a token.")

    def B_usr(self, cs_sock, sen_name, msg):
        print("b_usr: "+sen_name.decode("UTF-8").strip()+", "+msg.decode("UTF-8").strip())
        for client in self.CONNECTION_LIST:
            if client[1] != cs_sock:
                # client[1].send(sen_name)
                client[1].send(sen_name + ":".encode('UTF-8').strip() + msg)

# if __name__ == "__main__":
#     server = Server()
#     server.StartServer()
