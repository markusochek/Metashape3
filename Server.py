import socket

server = socket.socket()
port = 3000
server.bind(("localhost", port))
server.listen(5)

while True:
    con, addr = server.accept()
    data = con.recv(1024)
    if not data:
        break
    con.sendall(data)
    print(data.decode())
    con.close()
