import socket
import threading

# List to store all connected client sockets
connected_clients = []

def broadcast(message, sender_socket):
    # Send the message to all connected clients except the sender
    for client_socket in connected_clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except Exception as e:
                print(f"Error broadcasting message to a client: {e}")
                # Handle disconnection and remove the client from the list
                connected_clients.remove(client_socket)

def handle_client(client_socket):
    # Add the client socket to the list of connected clients
    connected_clients.append(client_socket)

    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Print the received message
            print(f"Received from {client_socket.getpeername()}: {data.decode('utf-8')}")

            # Broadcast the message to all other clients
            broadcast(data, client_socket)
        except Exception as e:
            print(f"Error handling client: {e}")
            break

    # Close the client socket and remove it from the list
    connected_clients.remove(client_socket)
    client_socket.close()

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(("127.0.0.1", 8888))

    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on port 8888...")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
