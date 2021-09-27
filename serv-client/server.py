from socket import socket , AF_INET , SOCK_STREAM
sobj=socket(AF_INET,SOCK_STREAM)
ip=input("Enter IP:- ")
port=input("Enter Port:- ")
sobj.bind((ip,port))
sobj.recv(1024)
sobj.listen(1)
client , addr = sobj.accept()
while True:
    recv=client.recv(1024).decode()
    print(recv)
    msg=input("Enter your text here:= ").encode()
    client.send(msg)
    client.close()