# SecureWall

A Python-based network traffic monitoring and rule-based firewall prototype.

## Features

- Captures live network packets using Scapy
- Supports TCP and UDP traffic
- Extracts source and destination IP addresses
- Extracts source and destination ports
- Applies configurable firewall rules
- Allows or blocks packets based on rules
- Logs packet information and firewall decisions
- Performs hostname lookup for destination IPs

## Project Structure

```text
SecureWall/
├── config/
│   ├── blocked_ips.txt
│   └── rules.txt
├── firewall/
│   ├── logger.py
│   ├── packet.py
│   ├── rules.py
│   └── sniffer.py
├── logs/
├── tests/
├── dashboard/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore

## Installation

1. Clone the repository:
      git clone https://github.com/vyshnavbalakrishnan17-png/SecureWall.git
2. Open the project folder:
      cd SecureWall
3. Install the required Python packages:
      pip install -r requirements.txt
4. Run SecureWall:
      python main.py      