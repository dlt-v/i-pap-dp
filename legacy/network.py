import socket
import pickle


class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.25.112.1"
        self.port: int = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def connect(self) -> str:
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data: str):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def get_p(self):
        return self.p
