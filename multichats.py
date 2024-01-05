import socket
import threading
clients=[]
def handleclient(client_socket,address):
	print(f"Connected to client {address}")
	while True:
		msg=client_socket.recv(1024).decode()
		print(f"\nMessage from client {address} =", msg)
		for client in clients:
			if client!=client_socket:
				try:
					client.send(msg.encode())
				except socket.error:
					clients.remove(client)
		if msg=='exit':
			break
	client_socket.close()
	print(f"connection with {address} closed")
	
def main():
	server_address=('localhost',12345)
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind(server_address)
	server_socket.listen()
	print("Server is listening")
	
	while True:
		client_socket,address=server_socket.accept()
		clients.append(client_socket)		
		client_thread=threading.Thread(target=handleclient,args=(client_socket,address))
		client_thread.start()


main()
	
