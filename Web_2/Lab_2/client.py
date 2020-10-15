from socket import *
import sys

host = 'localhost'
port = 777
addr = (host,port)
class d:
    def __init__(self, i, s):
        self.id = i
        self.surname = s
id=0
while id<16:
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setblocking(False)
    tcp_socket.connect_ex(addr)
    id=id+1
    cl=d(id,"Kharchenko")
    if not cl : 
        tcp_socket.close() 
        sys.exit(1)

    data = str.encode(cl.surname)
    tcp_socket.send(data)
    print(cl.id, cl.surname, "Connected") 

tcp_socket.close()
