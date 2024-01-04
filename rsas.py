import socket

def generatekey(p,q):
	n=p*q
	t=(p-1)*(q-1)
	e=3
	d=pow(e,-1,t)
	public_key=(e,n)
	private_key=(d,n)
	return public_key,private_key
	
def process(message,public_key,private_key):
	e,n=public_key
	d,n=private_key
	
	enc_msg=pow(message,e,n)
	dec_msg=pow(enc_msg,d,n)
	
	return enc_msg,dec_msg


def main():
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	server_socket.bind(server_address)
	server_socket.listen()
	print("server is listening")
	while True:
		client_socket,address=server_socket.accept()
		data=client_socket.recv(1024).decode()
		p,q,msg=map(int,data.split(','))
		pubk,pvtk=generatekey(p,q)
		enc_msg,dec_msg=process(msg,pubk,pvtk)
		res=f"publickey={pubk},privatekey={pvtk},encoded msg={enc_msg},decoded_msg={dec_msg}"
		client_socket.send(res.encode())
		
main()
		
