import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
server_socket.bind(('',port))
server_socket.listen(5)
print("Socket successfully created and now listening")

client_socket, addr = server_socket.accept()
print("Got connection from",addr)


    # client_socket.send("Thanks".encode())
    # client_socket.close()
    # break







