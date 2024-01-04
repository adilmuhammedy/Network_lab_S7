import socket

def decode(encoded_data):
	table={i: chr(i) for i in range(256)}
	old=encoded_data[0]
	s=table[old]
	c=s[0]
	decoded_data=s
	count=256
	for i in range(len(encoded_data)-1):
		n=encoded_data[i+1]
		if n not in table:
			s=table[old]+c
		else:
			s=table[n]
		
		decoded_data+=s
		c=s[0]
		table[count]=table[old]+c
		count+=1
		old=n
	return decoded_data


def main():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_address=('localhost',12349)
	client_socket.connect(server_address)
	inp=input("Enter the string to be encoded ")
	client_socket.send(inp.encode())
	encoded_data=client_socket.recv(1024).decode()
	print("encodeed data=", encoded_data.split(','))
	encoded_data=list(map(int, encoded_data.split(',')))
	decoded_data=decode(encoded_data)
	print(f"Original input: {inp}")
	print(f"Decoded output: {decoded_data}")
	
main()

