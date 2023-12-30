import socket

def caeser(text,key):
	result=""
	for char in text:
		if char.isalpha():
			offset=ord('A') if char.isupper() else ord('a')
			result+=chr((ord(char)-offset+key)%26+offset)
		else:
			result+=char
	return result
	
def main():
	data=input("Enter a string to encrypt: ")
	enc=caeser(data,3)
	print(f"Encrypted data= {enc}")
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	client_socket.connect(server_address)
	print(f"Connection established with {server_address}")
	client_socket.sendall(enc.encode('utf-8'))			
main()
