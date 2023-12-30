import socket
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('localhost',12345)
client_socket.connect(server_address)

while True:
	message=input("Enter a message to send to server: ")
	if message=="exit":
		break;
	client_socket.sendall(message.encode('utf-8'))
	response=client_socket.recv(1024)
	print("response from server= {}".format(response.decode('utf-8')))
client_socket.close()

