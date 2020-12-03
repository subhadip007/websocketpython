import  socket

c= socket.socket()

c.connect(('192.168.56.1',9999))

name= input('input your name here ')
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())

c.close()

