import socket

def caeser(text,key):
	result=""
	for char in text:
		if char.isalpha():
			offset=ord('A') if char.isupper() else ord('a')
			result+=chr((ord(char)-offset-key)%26+offset)
		else:
			result+=char
	return result
	
def main():
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	server_socket.bind(server_address)
	server_socket.listen(1)
	print("Server is listening")
	
	client_socket,address=server_socket.accept()
	print(f"Connection established with {address}")
	sdata=client_socket.recv(1024).decode()
	print("recieved data=",sdata)		
	print(f"decrypted data=",caeser(sdata,3))
main()
		
