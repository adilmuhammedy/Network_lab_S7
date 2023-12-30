import socket

def encrypt(text,key):
	result=""
	
	for char in text:
		if char.isalpha():
			shift=ord(char)+key
			if char.isupper():
				result+=chr((shift-ord('A'))%26 + ord('A'))
			else:
				result+=chr((shift-ord('a'))%26 + ord('a'))
	return result
	
def main():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	client_socket.connect(server_address)
	print(f"Connectted to server {server_address}")
	while True:
		data=input("Enter a message: (exit to quit): ")
		if data=="exit":
			break
		key=int(input("enter a key: "))
		enc=encrypt(data,key)
		print("Encrypted data= ", enc)
		client_socket.sendall(enc.encode('utf-8'))
	
	
main()
	
	
				

