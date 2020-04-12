import socket

import sys
import traceback

msg = 'We are waves of the same ocean, leaves of the same tree, flowers of the same garden'

def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print('connecting to {0} port {1}'.format(*server_address, file=log_buffer))
    
    try:
        sock.connect(server_address)
        my_message = msg
        sock.sendall(my_message.encode('utf-8'))
    
        received_message = sock.recv(4096)
        print("Server says: {}".format(received_message.decode(), file=log_buffer))
    
        sock.close()
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('closing socket') # TODO removed for testing , file=log_buffer
        sock.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python demo_client_01.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)