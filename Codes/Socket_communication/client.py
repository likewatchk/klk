import socket

HOST = '192.168.43.154' 
# Enter IP or Hostname of your server
PORT = 12345 
# Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("connected")

#Lets loop awaiting for your input
while True:
    command = input()
    command = command.encode(encoding='UTF-8')
    s.send(command)
    reply = s.recv(1024)
    reply = reply.decode("UTF-8")
    print(type(reply))
    if reply == 'Terminate':
        break
    print (reply)
