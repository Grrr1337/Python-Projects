# Simple Chat App (with sockets)

This is a simple client-server chat application implemented in Python using **sockets**. The server listens for incoming connections, and clients can connect to the server to exchange messages.

## Demo
Here is a demo where I use 4 separate terminal windows - the 1st one is running the server and the rest are the clients connected to it in order to chat together.

![Simple Chat App Demo](Simple%20Chat%20App%20Demo.gif)
## Usage

1. Run the server (`server.py`) to start listening for incoming connections.

    ```bash
    python server.py
    ```
    The server will be hosted at `127.0.0.1` on port `8888`.
    
2. Run one or more clients (`client.py`) to connect to the server. Create new __terminal__ instances for the new clients.

    ```bash
    python client.py
    ```

3. Enter messages in the client terminal to send them to the server. The server will broadcast the messages to all connected clients. Switch between the terminals in order to reproduce chat from different users.

4. Type 'exit' in a client to disconnect from the server.

## Project Structure

- `server.py`: Contains the server implementation.
- `client.py`: Contains the client implementation.

## Dependencies

- Python 3.x

## Notes

- This is a basic example and lacks production-level features and security measures.
- Error handling is minimal, and it's recommended to enhance it for a robust application.
- Consider using asynchronous programming or multiprocessing for scalability in a real-world scenario.

Feel free to explore and modify the code as needed for your requirements.
