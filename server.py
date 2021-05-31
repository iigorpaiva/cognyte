import socket
import random
import time
import json
from threading import Thread

clients = []
threads = [] 

##### generate a list of five random numbers ######
class dataStream(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.randomList = []

    def run(self):
        while(True):
            self.randomList = [random.randrange(1, 50, 1) for i in range(5)]
            #print(self.randomList)
            #time.sleep(1)

class ClientThread(Thread):

    def __init__(self,clientAddress,clientsocket, newDataStream):
        Thread.__init__(self)
        self.csocket = clientsocket
        print("New client connected: ", clientAddress)

        ##### Load randomlist made in dataStream Thread ######
        self.dataStream = newDataStream.randomList
        self.dataStream = json.dumps(self.dataStream)

    def run(self):
        print ("\n Connection from : ", clientAddress)
        while True:
            dataFromClient = self.csocket.recv(2048)
            messageFromClient = dataFromClient.decode()
            if messageFromClient=='end':
                  break
            print("Message from client: ", messageFromClient)
            self.csocket.sendall(self.dataStream.encode())

        print ("Client at ", clientAddress , " disconnected...")


##### Defining server #####
LOCALHOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))

print("Server started")
print("Waiting for client request..")

while True:
    
    newDataStream = dataStream()
    newDataStream.start()

    server.listen()
    clientsock, clientAddress = server.accept()

    newClientThread = ClientThread(clientAddress, clientsock, newDataStream)
    newClientThread.start()
