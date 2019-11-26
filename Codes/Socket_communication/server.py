import socket

<<<<<<< HEAD
HOST = '192.168.43.154' 
=======
HOST = '10.27.6.29' 
>>>>>>> 1c4d919da455dd6c7749cd7412b33ae93906e5fe
# Server IP or Hostname
PORT = 12345 
# Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
print('Socket created')

=======
print ('Socket created')
>>>>>>> 1c4d919da455dd6c7749cd7412b33ae93906e5fe
#managing error exception
try:
    s.bind((HOST, PORT))
except socket.error:
<<<<<<< HEAD
	print('Bind failed')

s.listen(5)
print('Socket awaiting messages')
(conn, addr) = s.accept()
print('Connected')

# awaiting for message
while True:
	data = conn.recv(1024)
	data = data.decode("UTF-8")
	print('I sent a message back in response to: ' + data)
	reply = ''

	# process your message
	if data == 'Hello':
		reply = 'Hi, back!'
	elif data == 'This is important':
		reply = 'OK, I have done the important thing you have asked me!'
	#and so on and on until...
	elif data == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'

	# Sending reply
	conn.send(reply.encode(encoding='UTF-8'))
    print ('Bind failed ')
s.listen(5)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')
# awaiting for message
while True:
    data = conn.recv(1024)
    data = data.decode(encoding='UTF-8')
    print (data)

conn.close() 
# Close connections

