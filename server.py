import socket
import threading

clients = []
nicknames = []

ip="127.0.0.1"
port=55556

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()


def broadcast(message):
    for client in clients:
        client.send(message)
    

def handler(client):
    while True:

        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            idx = clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[idx]
            broadcast(f'{nickname} left the chat! begin extermination')
            nicknames.remove(nickname)
            break

def recive():
    while True:
        client, address= server.accept()
        print(f'connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print('nickname of the client is {}'.format(nickname))
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('connected to server'.encode('ascii'))

        thread= threading.Thread(target= handler, args=(client, ))
        thread.start()

print("server is up")
recive()

