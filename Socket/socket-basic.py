import socket


tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.bind(("192.168.1.103", 2023))
tcpsocket.listen(2)


(client, (ip, port)) = tcpsocket.accept()
client.send(b"hello siyamak i am a server welcome!")
# client.recv(2024)


