from socket import socket , AF_INET , SOCK_STREAM
sobj=socket(AF_INET,SOCK_STREAM)
ip=input("Enter IP:- ")
port=input("Enter Port:- ")
sobj.connect((ip,port))
while True:
    msg=input("Enter your text here: ").encode()
    sobj.send(msg)
    recv=sobj.recv(1024).decode()
    print(recv)
    sobj.close()