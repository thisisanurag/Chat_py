# A basic chat server code using sockets and threading
import socket
import threading
ip="0.0.0.0"
port=90
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip,port))
sock.listen(1)
connections=[]
def handle(c,a):
    global connections
    while True:
        data=c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            c.close()
            connections.remove(c)
            break
while True:
    c,a=sock.accept()
    t=threading.Thread(target=handle, args=(c,a))
    t.daemon=True
    t.start()
    connections.append(c)
    print(connections)
