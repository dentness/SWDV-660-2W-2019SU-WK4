import socket

# constants
ADDRESS = ''
DEFAULT_BUFFER_SIZE = 4096
DEFAULT_ENCODING = 'UTF-8'
PORT = 9500

def call(msg: str, addr: str, port: int) -> str:
    """call a service with the provided msg.

    Args:
        msg: The body messsage sent to the service.
        addr: Address of the service.
        port: Port of the service, as an int.

    Returns:
        The decoded message from the service

    """
    s = socket.socket()
    s.connect((addr, port))
    s.send(msg.encode(DEFAULT_ENCODING))
    return s.recv(DEFAULT_BUFFER_SIZE).decode(DEFAULT_ENCODING)


def main():

    print(call('free willie', ADDRESS, PORT))
    print(call('Yo', ADDRESS, PORT))
    print(call('Hello', ADDRESS, PORT))
    print(call('Hi', ADDRESS, PORT))
    print(call('shutdown', ADDRESS, PORT))


if __name__ == "__main__":
    main()
