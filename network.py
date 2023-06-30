import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.2"  
        self.port = 65432
        self.addr = (self.server, self.port)
        self.pos = self.connect()
    
    def get_pos(self):
        return self.pos
       
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except Exception as e:
            print("Error connecting to the server:", str(e))
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except Exception as e:
            print("Error connecting to the server:", str(e))
            


