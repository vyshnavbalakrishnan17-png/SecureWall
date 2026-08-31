class RuleEngine:

    def __init__(self):
     with open("config/rules.txt", "r") as file:
        self.blocked_ports = [int(line.strip()) for line in file] 

     with open("config/blocked_ips.txt", "r") as file:
        self.blocked_ips = [line.strip() for line in file]

    def check(self, packet):
        if packet.source_ip in self.blocked_ips:
            return "BLOCK"
        if packet.destination_port in self.blocked_ports:
            return "BLOCK"

        return "ALLOW"