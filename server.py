import socket
import random
import time
import pickle
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
                time.sleep(2)
        
                #print("Message from client: ", messageFromClient)
                data = pickle.dumps(self.randomList)
                #print("DATA: ", data)
                print(self.randomList)
                self.csocket.sendall(data)
                pass

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
