import socket

c = socket.socket()

c.connect(('3.134.125.175',16439))
print("")
#name=input("Enter your name: ")
print("")
#print("")
#c.send(bytes(name,'utf-8'))
print("  *********************************")
print("")
print("    ",c.recv(1024).decode())  #,name +"\r\n"
print("")
print("  *********************************")
print("")
print("")
print(c.recv(1024).decode())