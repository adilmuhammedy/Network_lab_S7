import socket


def gen_hamcode(msg):
	r=0
	while 2**r <= len(msg)+r+1:
		r+=1
	
	data=list(msg)
	data.reverse()
	
	ham_code=[]
	c=0
	j=0
	
	for i in range (len(msg)+r):
		if 2**c == i+1:
			ham_code.append(0)
			c+=1
		  	
		else:
			ham_code.append(data[j])
			j+=1
	
	calc_parity(ham_code)
	ham_code.reverse()
	ham_code=int(''.join(map(str,ham_code)))
	return ham_code
	

def calc_parity(ham_code,parity_list=None):
	if parity_list is None:
		parity_list=[]
	
	c=0
	
	for parity in range(len(ham_code)):
		ph=2**c
		if (ph == parity+1) :
			start_index=ph-1
			i=start_index
			to_xor=[]
			
			while i<len(ham_code):
				block=ham_code[i:ph+i]
				to_xor.extend(block)
				i+=2*ph
				
			for z in range (1,len(to_xor)):
				ham_code[start_index]=int(ham_code[start_index])^int(to_xor[z])
			
			parity_list.append(ham_code[parity])
			c+=1
	
	print(parity_list)
	
	
def detect_and_correct():
	recv=input("Enter the Received Hamming code")
	data=list(recv)
	data.reverse()
	
	parity_list=[]
	
	calc_parity(data,parity_list)
	
	decimal=int(''.join(map(str,parity_list)),2)
	
	if(decimal==0):
		print("No error\n")
	else:
		print(f'Error at {decimal}th position')
	
	
	

def main():
	server_soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_soc.bind(('127.1.0.0',4000))
	server_soc.listen(1)
	
	client,addr=server_soc.accept()
	print(f'Client connection from:{addr}')
	
	msg=client.recv(1024).decode('utf-8')
	
	ham=gen_hamcode(msg)
	
	print(f'Hamming code msg is {ham}')
	
	print("Moving to error check and correct....")
	
	detect_and_correct()
	
	client.close()
	server_soc.close()
	
main()
