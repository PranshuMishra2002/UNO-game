import socket

s = socket.socket() 
print('socket created') 

s.bind(('127.0.0.1',12345))  # port number varies from: (0 -> 65535) 
                            #ipv4 -> 192.168.0.24
                            # 192.168.0.24

s.listen(3)
print('waiting for connection')

while True :
    c , addr = s.accept() 
    #name=c.recv(1024).decode('utf-8')
    print("connected with ",addr) 

    c.send(bytes('welcome to Uno game','utf-8'))
    c.send(bytes('lests play uno','utf-8'))

    c.close() 