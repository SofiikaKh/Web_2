from socket import *
import threading
import time
from threading import Timer
import datetime
import xml

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(10)

listClients = []
listconnections =[]
i=0
startTimer=0
def printing(list1):
    for i in range(len(listClients)):
        print(listClients[i])

def timeout():
    now = datetime.datetime.now()
    print ("timestartat:  ",now.strftime("%d-%m-%Y %H:%M"))
    printing(listClients)

t = Timer(10, timeout)
def sending(listClients):
    for i in range (len(listClients)):
        ur_sk = listconnections[i]
        x = XML.dumps(listClients) 
        ur_sk.send(x.encode("utf-8"))
        i =i+1

while True: 
    print('wait connection...')
    conn, addr = tcp_socket.accept()
    conn.setblocking(False)
    data = conn.recv(1024)
    listconnections.append(conn)
    if not data:
        break
    else:
        i=i+1
        if (i==1):
            t.start()
        print(i,bytes.decode(data), "connected")
        tnow=datetime.datetime.now()
        listClients.append([tnow.strftime("%d-%m-%Y %H:%M"),i,data])    
 
else: 
    for conn in listconnections:
        sending(listClients)
    for conn in listconnections:
        conn.close
    print("The end")


