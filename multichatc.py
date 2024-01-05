import socket
import threading

def recvmsgs(client_socket):
	while True:
		try:
			msg=client_socket.recv(1024).decode()
			print(f"Message from client",msg)
		except socket.error as e:
			print(f"Error recieving message: {e}")
			break

def main():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	try:
		client_socket.connect(server_address)
	except socket.error as e:
		print(f"Unable to connect to {e}")
		exit()
	recv_thread=threading.Thread(target=recvmsgs,args=(client_socket,))
	recv_thread.start()
	while True:
		message=input("ENter a message: ")
		client_socket.send(message.encode())
		if message=='exit':
			break
	client_socket.close()
main()
