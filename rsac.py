import socket

def main():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	client_socket.connect(server_address)
	msg=input("Enter a message to send: ")
	p=input("Enter p value: ")
	q=input("Enteer q value: ")
	data=f"{p},{q},{msg}"
	client_socket.send(data.encode())
	res=client_socket.recv(1024).decode()
	print(res)
	
	
main()
	


