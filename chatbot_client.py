import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
	try:
		sock.connect(('127.0.0.1',8000))
	except :
		sock.connect(('127.0.0.1',8080))
	message=sock.recv(4096)
	print (message.decode())
	print ('''
You Can Ask The Following Questions To Bot(enter quit to exit):
	1. Fee
	2. Outline
	3. Duration

	''')
	while True:
		msg=input("<<client>>")
		msg=msg.encode()
		sock.send(msg)
		reply=sock.recv(4096).decode()
		print (reply)
		if reply=="Connection Terminated":
			sock.close()
			exit(0)
