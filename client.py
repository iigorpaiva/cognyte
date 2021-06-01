import socket
import json
import datetime
import pickle
import time

import logging
from logging.handlers import RotatingFileHandler

##### Load configuration file ######
file = open("configuration.json", "r")
configurationFile = json.load(file)

SERVER =  configurationFile['Defaults']['server']
PORT = configurationFile['Defaults']['port']
SIZEFILE = configurationFile['Defaults']['sizeSavedFiles']
PREFIX = configurationFile['Defaults']['prefix']
TIMER = configurationFile['Defaults']['timer']

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Requesting data to server",'UTF-8'))
client.settimeout(TIMER)

##### Define today's date to concate ######
auxDateToday = datetime.datetime.now()
dateToday = auxDateToday.strftime("%Y%m%d%H%M%S")

#### function to Save data into a file ######
def createRotatingLog(path, content):

    ##### Creates a rotating log #####
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    
    ##### add a rotating handler #####
    handler = RotatingFileHandler(path, maxBytes=SIZEFILE,
                                  backupCount=0)
    logger.addHandler(handler)
    logger.info(content)

print("""                   _              _              _   
   ___ ___   __ _ _ __  _   _| |_ ___    ___| (_) ___ _ __ | |_ 
  / __/ _ \ / _` | '_ \| | | | __/ _ \  / __| | |/ _ \ '_ \| __|
 | (_| (_) | (_| | | | | |_| | ||  __/ | (__| | |  __/ | | | |_ 
  \___\___/ \__, |_| |_|\__, |\__\___|  \___|_|_|\___|_| |_|\__|
            |___/       |___/                                   """)

while True:

  ##### Receive data from server #####
  dataFromServer =  pickle.loads(client.recv(2048))
  #dataFromServer =  client.recv(2048)

  print("\n From Server : " , dataFromServer)

  ##### Call function to storage data locally ######
  log_file  = PREFIX + "_" + dateToday + ".log"
  createRotatingLog(log_file, dataFromServer)
  
#client.close()
