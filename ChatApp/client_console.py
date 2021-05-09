import socket, threading
class Client():

    def __init__(self):
        self.cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_send = threading.Thread(target = self.send)
        self.thread_receive = threading.Thread(target = self.receive)

    def StartClient(self):
        HOST = 'localhost'
        PORT = 5023
        self.cli_sock.connect((HOST, PORT))
        print('Connected to remote host...')
        uname = input('Enter your name to enter the chat > ')
        uname = uname.encode("UTF-8").strip()
        self.cli_sock.send(uname)

        self.thread_send.start()
        self.thread_receive.start()

    def send(self):
        while True:
            msg =input('\nMe: \n')
            self.cli_sock.send(msg.encode("UTF-8").strip())

    def receive(self):
        while True:
            sen_name = self.cli_sock.recv(1024).decode("UTF-8").strip()
            data = self.cli_sock.recv(1024).decode("UTF-8").strip()

            print('\n' + str(sen_name) + ' > ' + str(data)+'\n')
            print("Me:")


if __name__ == "__main__":
    client = Client()
    client.StartClient()
