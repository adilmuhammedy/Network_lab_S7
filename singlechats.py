import socket
	
server_address=('localhost',12346);
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
server_socket.bind(server_address);
server_socket.listen()
print("Server is listening");
client_socket,address=server_socket.accept();
print(f"connected to client {address}")
while True:
	msg=client_socket.recv(1024).decode();
	print("MEssage from client= ", msg)
	client_socket.send(msg.encode())
	if(msg=='exit'):
		break

	
