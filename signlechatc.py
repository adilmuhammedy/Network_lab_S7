import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
server_address=('localhost',12346);
client_socket.connect(server_address);
while True:
	msg=input("Enter a message to send to server: ");
	client_socket.send(msg.encode())
	resp=client_socket.recv(1024).decode()
	print("response from server= ",resp)
	if(resp=='exit'):
		break
	
	
