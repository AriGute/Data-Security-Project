import socket, threading
import ChatApp.Confirmation as Confirmation

def send():
    while True:
        msg =input('\nMe: \n')
        cli_sock.send(msg.encode("UTF-8").strip())

def receive():
    while True:
        sen_name = cli_sock.recv(1024).decode("UTF-8").strip()
        data = cli_sock.recv(1024).decode("UTF-8").strip()

        print('\n' + str(sen_name) + ' > ' + str(data)+'\n')
        print("Me:")

if __name__ == "__main__":
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5023
    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')
    uname = input('Enter your name to enter the chat > ')
    uname = uname.encode("UTF-8").strip()
    ConFunction=Confirmation.login(uname.decode("utf-8"))
    print("The Password:" + ConFunction)
    cli_sock.send(uname)

    thread_send = threading.Thread(target = send)
    thread_send.start()

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()