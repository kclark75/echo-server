import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    address = ('127.0.0.1', 10000)
    
    sock.bind(address)
    sock.listen(1)
    
    connection, client_address = sock.accept()
    
    buffer_size = 4096
    received_message = connection.recv(buffer_size)
    
    print("Client says: {}".format(received_message.decode()))

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address, file=log_buffer))
    
    connection.sendall(received_message.decode())

if __name__ == '__main__':
    server()
    sys.exit(0)