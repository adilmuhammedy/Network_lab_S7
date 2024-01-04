import socket
def encode(data):
	table={chr(i):i for i in range(256)}
	p=data[0]
	code=256
	output=[]
	
	print("string\tOutput code\t Addition")
	i=0
	while i<len(data):
		if i!=len(data)-1:
			c=data[i+1]
		if p+c in table:
			p=p+c
		else:
			output.append(table[p])
			print(f"{p}\t{table[p]}\t\t{p+c}\t{code}")
			table[p+c]=code
			p=c
			code+=1
			
		i+=1
	output.append(table[p])
	print(f"{p}\t{table[p]}")
	return output
	
def main():
	server_address=('localhost',12349)
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_socket.bind(server_address)
	server_socket.listen()
	print("server  is listeniing")
	
	while True:
		conn,adr=server_socket.accept()
		print(f"Connected to {adr}")
		data=conn.recv(1024).decode()
		encoded_data=encode(data)
		print(f"Encoded data= {encoded_data}")
		conn.sendall(','.join(map(str,encoded_data)).encode())
		print("Encoding compppleted")
		conn.close()
main()
	
	
