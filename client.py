import sys
import socket
import select as sel

RECEIVE_BUFF = 4096

def chat_client():
    if len(sys.argv) < 3:
        print("Usage: python3 {} hostname port".format(sys.argv[0]))
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        s.connect((host, port))
    except:
        print("Cannot reach {}:{}".format(host, port))
        sys.exit(-1)

    print("Connected to remote host. You can start sending messages...")
    sys.stdout.write("> ")
    sys.stdout.flush()

    SOCKET_LIST = [sys.stdin, s]

    try:
        while True:
            read_ready, write_ready, error = sel.select(SOCKET_LIST, [], [])

            for sock in read_ready:
                # Incoming message from server
                if sock == s:
                    data = sock.recv(RECEIVE_BUFF)

                    if not data:
                        print("\nServer disconnected.")
                        return
                    else:
                        sys.stdout.write(data.decode())
                        sys.stdout.write("> ")
                        sys.stdout.flush()

                # User input
                else:
                    msg = sys.stdin.readline()
                    if msg.strip().lower() == "exit":
                        print("Closing connection...")
                        return

                    s.send(msg.encode())
                    sys.stdout.write("> ")
                    sys.stdout.flush()

    except KeyboardInterrupt:
        print("\nInterrupted by user")

    finally:
        print("Cleaning up socket...")
        try:
            s.shutdown(socket.SHUT_RDWR)
        except:
            pass
        s.close()


if __name__ == "__main__":
    sys.exit(chat_client())