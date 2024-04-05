import socket
from base64 import b64encode, b64decode

# 模拟一个http server
server = socket.socket()
server.bind(('0.0.0.0', 2345))
server.listen(512)

resp_data = 'HTTP/1.1 200 OK\r\nserver: SB\r\n\r\nxwp is handsome'
while True:
    client, cli_addr = server.accept()
    data = client.recv(1024)
    print('Received data: ',data.decode())
    client.send(resp_data.encode())
    client.close()
