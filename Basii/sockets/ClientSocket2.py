#file ClientSocket2.py
import socket
 
def Main(Na):
        host = '127.0.0.1'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = raw_input(" -> ")
         
        while message != 'q':
                message = message + "<from>" + Na + "</from>"
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = raw_input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Na = raw_input("your name? ")
    Main(Na)