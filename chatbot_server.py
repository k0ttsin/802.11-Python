import socket

scon=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address="127.0.0.1"
port=8000
try:
    scon.bind((address,port))
except:
    scon.bind((address,8080))
scon.listen()
print ("Waiting Connection")
connection,addr=scon.accept()
print ("Connected By :",addr)
message="Connected <message from server>"
connection.send(message.encode())
while connection:

    reply=connection.recv(1024).decode()
    
    if (reply in "Course Outline") or (reply in "course outline"):
        mesg="1.Introduction\n2.StandardIO\n3.Conclusion"
        connection.send(mesg.encode())
    elif  (reply in "Course Duration") or (reply in "course duration"):
        mesg="2Days"
        connection.send(mesg.encode())
    elif  (reply in "Course Fee") or (reply in "course fee"):
        mesg="5000Kyates"
        connection.send(mesg.encode())
    elif (reply == "Quit") or (reply =="exit") or (reply == "quit"):
        
        mesg="Connection Terminated"
        connection.send(mesg.encode())
        connection.close()
        exit(0)
    else:
        mesg="Wrong Question"
        connection.send(mesg.encode())
