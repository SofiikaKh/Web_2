from socket import *
import sys

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect_ex(addr)
cl="Kharchenko"
if not cl : 
    tcp_socket.close() 
    sys.exit(1)
tcp_socket.send(cl.encode("utf-8"))
print(cl, "Connected") 

receive=tcp_socket.recv(1024).decode("utf-8")
print(receive)
input("")