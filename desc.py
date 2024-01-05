import socket
from Crypto.Cipher import DES
import binascii

def pad(text):
	while(len(text)%8)!=0:
		text+=' '
	return text

def encrypt(plaintext, key):
	des=DES.new(key, DES.MODE_ECB)
	return des.encrypt(plaintext)
	
def main():
	client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address=('localhost',1234)
	client_socket.connect(server_address)
	plaintext=input("Enter a text: ")
	paddedpt=pad(plaintext).encode('utf-8')
	key=b'8bytekey'
	enc=encrypt(paddedpt,key)
	print("encrypted msg= ",enc)

	client_socket.send(enc)
main()
	
