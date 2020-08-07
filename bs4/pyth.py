import socket
import BeautifulSoup
s_name=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_name.connect('host',port)
cmd='GET URL port'.encode()
s_name.send(cmd)

while True:
	data=s_name.recv(512)
	if(len(data)<1):
		break
	print(data.decode())
s_name.close()