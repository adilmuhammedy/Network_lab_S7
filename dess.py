import socket
from Crypto.Cipher import DES
import binascii

def pad(text):
	print("Length of text=", len(text))
	while(len(text)%8)!=0:
		text+=" "
	return text
	
def decrypt(ciphertext,key):
	des=DES.new(key,DES.MODE_ECB)
	return des.decrypt(ciphertext)
	
	
def main():
	server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address=('localhost', 1234)
	server_socket.bind(server_address)
	server_socket.listen(1)
	print("SERver is listening")
	client_socket,address=server_socket.accept()
	ct=client_socket.recv(1024)
	print("Enncrypted msg  recieved= ", ct)
	key=b'8bytekey'
	pt=decrypt(ct,key)
	pt=pt.decode('utf-8')
	print("decrypted msg= ",pt)

	
main()
