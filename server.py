import socket

"""
SWDV 660 2W 19/SU1
Joe Dent
Week 4 Assignment
"""

# Constants
ADDRESS = ''
DEFAULT_BUFFER_SIZE = 4096
DEFAULT_ENCODING = 'UTF-8'
MAX_CONNECTIONS = 100
PORT = 9500
SHUTDOWN_KEYWORD = 'shutdown'


def generate_response(msg: str) -> str:
    """call a service with the provided msg.

    Args:
        msg: The body messsage sent to the service.
        addr: Address of the service.
        port: Port of the service, as an int.

    Returns:
        The decoded message from the service

    """
    if msg == 'Hello':
        return 'Hi'
    else:
        return 'Goodbye'


def listen_and_handle_requests(svr: socket) -> None:
    """listen for requests and process responses

    Args:
        svr: The socket server to listen on.


    Returns:
        None

    """
    svr.listen(MAX_CONNECTIONS)
    done = False
    while not done:
        conn, addr = svr.accept()
        msg = conn.recv(DEFAULT_BUFFER_SIZE).decode(DEFAULT_ENCODING)
        done = msg == SHUTDOWN_KEYWORD
        conn.send(generate_response(msg).encode(DEFAULT_ENCODING))
        conn.close()


def main():
    # Configure server
    s = socket.socket()
    s.bind((ADDRESS, PORT))

    # Process requests
    listen_and_handle_requests(s)


if __name__ == "__main__":
    main()
