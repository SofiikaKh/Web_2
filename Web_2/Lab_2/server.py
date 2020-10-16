from socket import *
import threading
import time
from threading import Timer
import datetime
import xml.etree.ElementTree as ET

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

def timeout():
    now = datetime.datetime.now()
    print ("timestartat:  ",now.strftime("%d-%m-%Y %H:%M"))
    sending(listClients)

t = Timer(10, timeout)
def sending(listClients):
    root = ET.Element("LIST")  # рутовый элемент
    for i in range (len(listClients)):
        query = ET.SubElement(root, "time")  # добавляем дочерний элемент к root
        query.text = str(listClients[i][0])  # добавляем значение элемента
        query = ET.SubElement(root, "id")  # добавляем дочерний элемент к root
        query.text = str(listClients[i][1])  # добавляем значение элемента
        query = ET.SubElement(root, "surname")  # добавляем дочерний элемент к root
        query.text = str(listClients[i][2])  # добавляем значение элемента
        message = ET.tostring(root, "utf-8")
        doc = '<?xml version="1.0" encoding="UTF-8"?>' + message.decode("utf-8")
        print (doc)
    for i in range (len(listconnections)):
        ur_sk=listconnections[i]
        ur_sk.send(doc.encode("utf-8"))
while i<16: 
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
        conn.close
    print("The end")


