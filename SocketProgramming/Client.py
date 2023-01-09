import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',9996))
name=input("Enter name:")
c.send(bytes(name,'utf-8'))
msg=c.recv(1024)
print(msg.decode("utf-8"))