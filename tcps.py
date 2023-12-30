import socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address=('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
client_socket,client_address=server_socket.accept()
print("Connected to client {}" .format(client_address))

while True:
	data=client_socket.recv(1024).decode('utf-8')
	if data=="hi":
		response = "HEllo"
	elif data=="exit":
		response="closed connection"
		break;
		
	else:
		response="DaTA UNAVAILAble"

	client_socket.sendall(response.encode('utf-8'))
server_socket.close()




