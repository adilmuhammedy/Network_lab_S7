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
			cipher=xor(cipher, "0"*clength)+data[clength]
		clength+=1
	if cipher[0]=="1":
		cipher=xor(cipher,key)
	else:
		cipher=xor(cipher, "0"*clength)
	return cipher
	

def main():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12345)
	client_socket.connect(server_address)
	msg=input("Enter a messsage to send: ")
	paddedmsg=msg+"0"*(len(key)-1)
	rem=div(paddedmsg,key)
	enc=msg+rem
	print("encrypted message= ", enc)
	client_socket.send(enc.encode())
	
main()
