import socket
from scapy.all import sniff
from datetime import datetime



from firewall.packet import Packet
from firewall.rules import RuleEngine
from firewall.logger import Logger

rule_engine = RuleEngine()
logger = Logger()


def packet_callback(packet):
    # Process only IP packets
    if not packet.haslayer("IP"):
        return

    source_ip = packet["IP"].src
    destination_ip = packet["IP"].dst
   #time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        hostname = socket.gethostbyaddr(destination_ip)[0]
    except:
        hostname = "Unknown"

    if packet.haslayer("TCP"):
        source_port = packet["TCP"].sport
        destination_port = packet["TCP"].dport
        protocol = "TCP"

    elif packet.haslayer("UDP"):
        source_port = packet["UDP"].sport
        destination_port = packet["UDP"].dport
        protocol = "UDP"

    else:
        return

    real_packet = Packet(
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        protocol
    )

    decision = rule_engine.check(real_packet)
    logger.log(real_packet, decision)

    print("==============================")
    print(f"Time           : {current_time}")
    print(f"Source IP      : {source_ip}")
    print(f"Destination IP : {destination_ip}")
    print(f"Hostname       : {hostname}")
    print(f"Protocol       : {protocol}")
    print(f"Source Port    : {source_port}")
    print(f"Destination Port: {destination_port}")
    print(f"Decision       : {decision}")
    print("==============================")


def start_sniffer():
    print("Sniffer Started...")
    sniff(prn=packet_callback, count=5)