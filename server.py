import socket

s = socket.socket()

print('socket created')
server= socket.gethostbyname(socket.gethostname())
s.bind((server,9991))
s.listen(3)

print('waiting for the connceetion')

while True:
    c, addr=s.accept()
    name = c.recv(1024).decode()
    print('conncted with ',addr,name)

    c.send(bytes('welcome noob','utf-8'))
    c.close()