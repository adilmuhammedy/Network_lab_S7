import socket

def decrypt(text,key):
	result=""
	
	for char in text:
		if char.isalpha():
			shift=ord(char)-key
			if char.isupper():
				result+=chr((shift-ord('A'))%26 + ord('A'))
			else:
				result+=chr((shift-ord('a'))%26 + ord('a'))
	return result

def main():
	server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address=('localhost',12345)
	server_socket.bind(server_address)
	server_socket.listen(1)
	print(f"server listening to {server_address}")
	client_socket,client_address=server_socket.accept()
	while True:
		data=client_socket.recv(1024).decode('utf-8')
		print("recieved data= ", data)
		key=int(input("Enter the key:(press 0 to exit) "))
		if key==0:
			break		
		dec=decrypt(data,key)
		print("Decrypted data= ", dec)
	
	server_socket.close()
	
main()
	
