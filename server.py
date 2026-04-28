import socket as s
import select as sel
import sys

HOST = ''
PORT = 4444
SOCKET_LIST = []
RECEIVE_BUFF = 4096

def chat_server():
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)

    print("Chat server started on port " + str(PORT) + "...")

    try:
        while True:
            ready_read, _, _ = sel.select(SOCKET_LIST, [], [])

            for sock in ready_read:

                #  New connection
                if sock == server_socket:
                    client_socket, addr = server_socket.accept()
                    SOCKET_LIST.append(client_socket)

                    print("Client {}:{} connected".format(addr[0], addr[1]))

                    broadcast(server_socket, client_socket,
                              "{} entered the chat\n".format(addr))

                # 🔹 Incoming message
                else:
                    try:
                        data = sock.recv(RECEIVE_BUFF)

                        if not data:
                            raise Exception("Disconnected")

                        message = data.decode()

                        # Print on server
                        print("Message from {}: {}".format(sock.getpeername(), message))

                        broadcast(server_socket, sock,
                                  "[{}] {}".format(sock.getpeername(), message))

                    except:
                        try:
                            addr = sock.getpeername()
                        except:
                            addr = "Unknown"

                        print("Client {} disconnected".format(addr))

                        broadcast(server_socket, sock,
                                  "[{}] Client is Offline".format(addr))

                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        sock.close()

    except KeyboardInterrupt:
        print("\nServer shutting down...")

    finally:
        for sock in SOCKET_LIST:
            sock.close()


def broadcast(server_socket, client_socket, message):
    for socket in SOCKET_LIST:
        if socket != server_socket and socket != client_socket:
            try:
                socket.send(message.encode())
            except:
                socket.close()
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)


if __name__ == "__main__":
    sys.exit(chat_server())