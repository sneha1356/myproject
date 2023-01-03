import socket
s=socket.socket()
print("Socket Created")
s.bind(("localhost",9998))
s.listen(3)
print("waiting for connection")
while True:
    client,address=s.accept()
    name=client.recv(1024).decode()
    print("connection with",address)
    client.send(bytes("welcome to hcl",'utf-8'))
    client.close()