import socket
import threading
from sys import exit

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("127.0.0.1", 55556))

nickname=input('Pls Enter a nickname')

def recive():
    while True:
        try:
            message=server.recv(1024).decode("ascii")
            if message == "NICK":
                server.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('an error occurred')
            server.close()
            break

def write():
    while True:
        try:
            message=f'{nickname}: {input("")}'
            server.send(message.encode('ascii'))
        except:
            exit()

recive_thread=threading.Thread(target=recive)
recive_thread.start()

write_thread= threading.Thread(target=write)
write_thread.start()
