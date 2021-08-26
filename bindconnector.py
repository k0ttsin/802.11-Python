import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
	try:
		sock.connect(('127.0.0.1',8000))
	except :
		sock.connect(('127.0.0.1',8080))
	print ("Connected To Target")
	while True:
		command=input("<<shell@target|$")
		sock.send(command.encode())
		if command=="exit":
			sock.close()
			exit(0)
		result=sock.recv(4096)
		print (result.decode())
