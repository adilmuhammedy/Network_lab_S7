import socket
key="1101"

def xor(a,b):
	res=[]
	for i in range(1,len(a)):
		if a[i]==b[i]:
			res.append("0")
		else:
			res.append("1")
	return "".join(res)

def div(data,key):
	clength=len(key)
	cipher=data[0:clength]
	while clength<len(data):
		if cipher[0]=="1":
			cipher=xor(cipher,key)+data[clength]
		else:
			cipher=xor(cipher,"0"*len(key))+data[clength]
		clength+=1
	if cipher[0]=="1":
		cipher=xor(cipher,key)
	else:
		cipher=xor(cipher,"0"*len(key))
	return cipher
				

def main():
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	server_socket.bind(server_address)
	server_socket.listen()
	print("Server is listening")
	client_socket,addr=server_socket.accept()
	enc=client_socket.recv(1024).decode()
	enc=enc+"0"*(len(key)-1)
	rem=div(enc,key)
	print("remainder= ",rem)
	check="0"*(len(key)-1)
	if(rem==check):
		print("no error")
	else:
		print("Error is there")
		
main()
		
	
