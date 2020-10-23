from socket import *
import threading
import time
from threading import Timer
import datetime
import xml.etree.ElementTree as ET
import select

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen(16)

listClients = []
listconnections =[]
i=0
startTimer=0

wait=10
r=[] 
w=[] 
requests=0

def listconnections_read(r_clients, clientlist):
    responses={}
    for tcp_socket in r_clients:
        try:
            data= sock.recv(1024).decode("utf-8")
            responses[tcp_socket]=data
        except:
            print("client{}{}disconnected".format(tcp_socket.fileno(),tcp_socket.getpeername()))
            listconnections.remove(tcp_socket)
    return  responses
def xmlcreate(listClients):
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
    return doc
def listconnections_write(requests, w_clients, all_clients):
    for tcp_socket in w_clients:
        if tcp_socket in requests:
            try:
                response = xmlcreate(listClients)
                tcp_socket.send(response.encode("utf-8"))
            except:
                print("client{}{}disconnected".format(tcp_socket.fileno(),tcp_socket.getpeername()))  
                tcp_socket.close()
    return response
def timeout():
    now = datetime.datetime.now()
    print ("timestartat:  ",now.strftime("%d-%m-%Y %H:%M"))
    if  requests:
        listconnections_write(requests,w,listconnections)
t = Timer(10, timeout)
while i<16: 
    print('wait connection...')
    conn, addr = tcp_socket.accept()
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
      
        try:
            r,w,e = select.select(listconnections,listconnections,[],wait)  
        except: 
            pass
        requests = listconnections_read(r,listconnections)
       
else: 
    print("The end")


print ("xmll,",xmlcreate(listClients))

