import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created")
s.bind(('localhost',9996))
s.listen()
print("waiting for connection")
while True:
    client,address=s.accept()
    name=client.recv(1024).decode()
    print("connection with",address)
    client.send(b"welcome to hcl")
    client.close()