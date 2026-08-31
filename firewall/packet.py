class Packet:
    def __init__(self, source_ip, destination_ip, source_port, destination_port, protocol):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.protocol = protocol

    def display(self):
        print(f"Source IP: {self.source_ip}")
        print(f"Destination IP: {self.destination_ip}")
        print(f"Source Port: {self.source_port}")
        print(f"Destination Port: {self.destination_port}")
        print(f"Protocol: {self.protocol}")