import zmq
import time

context = zmq.Context()

# ROUTER socket binds to a specific IP and port
router_socket = context.socket(zmq.ROUTER)
router_socket.bind("tcp://127.0.0.1:5555")

clients = {}

while True:
    # Poll sockets for messages
    sockets = dict(context.poll(1000, zmq.POLLIN, router_socket))

    # Handle incoming message from a client
    if router_socket in sockets:
        # Receive the client identity and message
        identity, message = router_socket.recv_multipart()

        # Add client to list if not already present
        if identity not in clients:
            clients[identity] = context.socket(zmq.DEALER)
            clients[identity].connect("tcp://" + identity.decode())

        # Forward message to all other clients
        for client_identity, client_socket in clients.items():
            if client_identity != identity:
                client_socket.send_multipart([identity, message])

    # Send a ping message to all clients to check if they are still alive
    for client_identity, client_socket in clients.items():
        client_socket.send(b"PING")

        # If the client does not respond within 1 second, assume it's dead and remove it from the list
        if client_socket not in sockets:
            print(f"Client {client_identity.decode()} is dead.")
            client_socket.close()
            del clients[client_identity]

    time.sleep(0.1)
