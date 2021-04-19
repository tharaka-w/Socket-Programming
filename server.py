import socket
import threading #creating multiple threads in one python prof
HEADER=64
PORT = 5050 # in computer we have number of portscleaea


#SERVER= '192.168.1.100' #bcs i run the server on this same computer
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR=(SERVER,PORT) #Creating a tuple
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
#Socket opensup our device to other networks
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Created the socket
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"NEW CONNECTION {addr} connected")
    connected=True
    while connected:
        msg_length= conn.recv(HEADER).decode(FORMAT) #How many bits we recieve 
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] {msg}")

    conn.close()

    

def start():
    server.listen()
    print(f"[Listening] {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr)) #when a new connection occurs that is passed to handle clietnts

        thread.start()
        print(f"ACTIVE CONNECTIONS {threading.activeCount()-1}") #Find active threads

    

print("Starting server is starting")
start()
