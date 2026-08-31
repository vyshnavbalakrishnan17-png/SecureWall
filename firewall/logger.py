class Logger:

    def log(self, packet, decision):
        with open("logs/firewall.log", "a") as file:
            file.write(
                f"Source IP: {packet.source_ip} | "
                f"Destination IP: {packet.destination_ip} | "
                f"Source Port: {packet.source_port} | "
                f"Destination Port: {packet.destination_port} | "
                f"Protocol: {packet.protocol} | "
                f"Decision: {decision}\n"
            )