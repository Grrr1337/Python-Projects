import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive data from the server
            data = client_socket.recv(1024)
            if not data:
                break

            # Print the received message
            print(f"Received from server: {data.decode('utf-8')}")
        except Exception as e:
            print(f"Error: {e}")
            break

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(("127.0.0.1", 8888))
    print("Connected to the server.")

    # Start a new thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Send messages to the server
        message = input("Enter your message (type 'exit' to quit): ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            break

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()
