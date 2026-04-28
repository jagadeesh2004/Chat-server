# 💬 Multi-Client Chat Server (Python)

A simple **multi-client chat application** built using Python socket programming.

This project demonstrates how multiple clients can connect to a single server over the same port and communicate in real time.

The server uses **I/O multiplexing (`select`)** to efficiently handle multiple connections without using threads.

---

## 🧾 About

- Multi-client communication over a single port  
- Real-time message broadcasting  
- Efficient connection handling using `select()`  
- Graceful client disconnect handling  

---

## ⬇️ Download

Clone the repository:

```bash
git clone https://github.com/jagadeesh2004/Chat-server.git
cd Chat-server

---------------------------------------------------------------

## ▶️ Run

Start the server

python3 server.py

Next start the client

$ python3 client.py <server-ip> <port>

You can open multiple terminals to simulate multiple clients

----------------------------------------------------------------

🖥️ Server

+ Listens on a specified port (4444)
+ Accepts multiple client connections
+ Broadcasts messages to all connected clients
+ Handles client disconnects gracefully

-----------------------------------------------------------------

💻 Client
+ Connects to server using IP and port
+ Sends user input to server
+ Receives and displays messages from other clients
+ Supports clean exit

-----------------------------------------------------------------

🧪 Example

Terminal 1 (Server)

    python3 server.py

Terminal 2 (Client 1)

    python3 client.py 127.0.0.1 4444

Terminal 3 (Clinet 2)

    python3 client.py 127.0.0.1 4444


-----------------------------------------------------------------

⚙️ Requirements

+ Python 3.x
+ Works on Linux / Windows / macOS

-----------------------------------------------------------------

🚀 Future Improvements

+ Add username support
+ Implement multithreading version
+ Add encryption (SSL/TLS)
+ Build GUI interface

-----------------------------------------------------------------
