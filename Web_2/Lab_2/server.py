#Модуль socket для сетевого программирования
from socket import *
import threading
import time
from threading import Timer
import datetime



#данные сервера
host = 'localhost'
port = 777
addr = (host,port)

#socket - функция создания сокета 
#первый параметр socket_family может быть AF_INET или AF_UNIX
#второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_socket = socket(AF_INET, SOCK_STREAM)
#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)
#listen - запускает прием TCP
tcp_socket.listen(10)

#Бесконечный цикл работы программы


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
def message(listClients):
    print("15")


while True: 
    print('wait connection...')
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    #устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    conn, addr = tcp_socket.accept()
    conn.setblocking(False)
    data = conn.recv(1024)
    listconnections.append(conn)
    #если ничего не прислали, завершим программу
    if not data:
        break
    else:
        i=i+1
        if (i==1):
            t.start()
        print(i,bytes.decode(data), "connected")
        tnow=datetime.datetime.now()
        listClients.append([tnow.strftime("%d-%m-%Y %H:%M"),i,data])
        #send - передает сообщение TCP
        #close - закрывает сокет
      #  conn.close()
        
    if (i==16):
        break
else: 
    for conn in listconnections:
        conn.sendall(b'Hello from server!')
    for conn in listconnections:
        conn.close
    print("The end")




tcp_socket.close()
