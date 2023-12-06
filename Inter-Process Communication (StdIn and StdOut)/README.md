# Inter-Process Communication with Python Executables

Executables can talk to each other!

Discover communication between different processes through pipes using Python executables. Processes can send and receive messages, exploring inter-process communication through __StdIn__ and __StdOut__.

The purposes of this project are explorational, so it may not have any direct practical application.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)



## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Grrr1337/Python-Projects.git
   ```

2. Ensure you have Python installed (version 3.x recommended).
3. Use an appropriate IDE such as VS Code or a Python-specific IDE like PyCharm.
4. Set up a virtual environment for the project:
    ```bash
    python -m venv .venv
    ```
5. Activate the virtual environment:
    On Windows:
    ```bash
    .venv\Scripts\activate
    ```
    On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```
6. Install the project dependencies using the provided requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```

## Getting Started

### Build the executables
To build the executables, adjust the parameters within the **main.py** file and run it.
```bash
python main.py
```
### Start a Conversation
To initiate a conversation, navigate to the dist directory and execute the following command in the terminal:
```bash
Person0.exe --message "{\"message\": \"Let's Talk\", \"counter\": 0, \"communication_limit\": 10}"
```

After the conversation is initiated:

- Each executable (e.g., Person0.exe) appends a randomly generated string to the communication message.
- The modified message is then passed to the next executable in the sequence.
- This process continues in a cyclical manner until Person5.exe talks back to Person0.exe.
- The conversation persists until the communication limit is reached.

This cyclical communication loop is enriched by appending random strings, showcasing the dynamic nature of inter-process communication, facilitated by the project.

## Usage

The project consists of three main components:

**CommunicationWrapper (communication_wrapper.py):**
- Manages communication between executables.
- Sends and receives messages through pipes.
- Handles counter and communication limits.

**ExeGenerator (ExeGenerator.py):**
- Dynamically generates executable files based on the CommunicationWrapper.
- Cleans up temporary files after generating executables.

**main.py:**
- Initiates a conversation by generating executables and calling the CommunicationWrapper.
- Feel free to customize the conversation by modifying the `arguments` variable in `main.py`.

## Project Structure

The project is structured as follows:

- **communication_wrapper.py:** Contains the CommunicationWrapper class for managing communication between executables.

- **ExeGenerator.py:** Defines the ExeGenerator class to dynamically create executable files for testing.

- **main.py:** Initiates the conversation by generating executables and calling the CommunicationWrapper.

Ensure to customize the project based on your requirements and explore the capabilities of inter-process communication.
