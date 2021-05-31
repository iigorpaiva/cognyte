import socket
import random
import time
import json
from threading import Thread

class ClientThread(Thread):

    def __init__(self,clientAddress,clientsocket):
        Thread.__init__(self)
        self.csocket = clientsocket
        print("\n New client connected: ", clientAddress)
        self.randomList = []

    def run(self):
        print ("Connection from : ", clientAddress)
        try: 
            while True:
                
                ##### Generate a lists with random numbers #####
                self.randomList = [random.randrange(1, 50, 1) for i in range(5)]
                time.sleep(0.5)
        
                #print("Message from client: ", messageFromClient)
                self.data_string = json.dumps(self.randomList)
                self.csocket.sendall(self.data_string.encode())
                #print(self.randomList)

                server.accept()

        except:
            print("Client ", clientAddress, "disconnected")

##### Defining server #####
LOCALHOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")

while True:

    server.listen()
    clientsock, clientAddress = server.accept()

    newClientThread = ClientThread(clientAddress, clientsock)
    newClientThread.start()
