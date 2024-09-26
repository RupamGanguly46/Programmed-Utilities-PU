import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 12345

# Connect to the server
client_socket.connect(('127.0.0.1', port))

print(client_socket.recv(1024).decode())

# Close the connection
client_socket.close()