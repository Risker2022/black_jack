import socket

class Socket():
    def __init__(self):
        # Makes the socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.start_msg = "connection accepted"
        self.client = []
        self.address = []
    
    def connect(self, ip, output_list=[], index=0):
        # Check for success of connection
        try:
            # Define needed variables
            port = 9999

            # Connect to the server
            print("Connecting to the server...")
            self.socket.connect((ip, port))

            print("Connected to the server!")
            if output_list:
                print("Returning True")
                output_list[index] = True
                return
            return True
        except:
            if output_list:
                output_list[index] = False
                return
            return False

    def create(self, listen_amount, output_list=[]):
        # Define needed variables
        ip = socket.gethostbyname(socket.gethostname())
        port = 9999

        # Create the server
        self.socket.bind((ip, port))
        self.socket.listen(listen_amount)

        # Accept the connection
        for _ in range(listen_amount):
            temp_client, temp_address = self.socket.accept()
            print(f"Connection from {temp_address} has been established!")
            self.client.append(temp_client)
            self.address.append(temp_address)
            output_list.append([temp_client, temp_address])

    def close(self):
        # Close the socket
        self.socket.close()

    def send(self, msg, client):
        # Send a message
        client.send(msg.encode("utf-8"))
    
    def get_ip(self):
        # Get the ip address
        return socket.gethostbyname(socket.gethostname())

    def recv(self):
        # Receive a message
        return self.socket.recv(4096).decode("utf-8")
