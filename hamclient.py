import socket


def main():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_socket.connect(('127.1.0.0',4000))
	
	data=input("Enter the data:\n")
	
	client_socket.send(data.encode('utf-8'))
	

main()
