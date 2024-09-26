import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 12345
# Bind to the port
server_socket.bind(('', port))

# Queue up to 5 requests
server_socket.listen(5)

print("Socket successfully created")
print("Socket binded to %s" % (port))
print("Socket is listening")

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    # Send a thank you message to the client
    client_socket.send('Thank you for connecting'.encode())

    # Close the connection
    client_socket.close()
    break