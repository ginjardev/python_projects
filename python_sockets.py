import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
my_socket.bind((host, port))
my_socket.listen(5)
while True:
    my_client, address = my_socket.accept()
    print(f'connected to {str(address)}')
    my_client.send(encode("ascii"))
    my_client.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))
msg = s.recv(1024)
s.close()

print(msg.decode('ascii'))