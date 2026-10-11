# SecureWall

A Python-based network traffic monitoring and rule-based firewall **prototype** built with
Scapy. It captures live packets, evaluates each one against configurable rules, and logs an
`ALLOW`/`BLOCK` decision.

> **Status: prototype / analysis tool.**
> SecureWall *monitors* traffic and *logs* what it would block. It does **not** drop or block
> packets at the network level — real enforcement would need OS-level integration (e.g.
> `iptables`/netfilter), which is future work.

## What it does

- Captures live IP packets using Scapy
- Reads TCP and UDP traffic
- Extracts source/destination IP addresses and ports
- Resolves destination hostnames via reverse DNS
- Evaluates each packet against configurable rules
  (`config/rules.txt` for blocked destination ports, `config/blocked_ips.txt` for blocked source IPs)
- Logs packet details and the decision to `logs/firewall.log`, and prints them

## Limitations (honest scope)

- **Logs decisions only** — it does not enforce blocking
- Captures a fixed batch of **5 packets** per run (`sniff(count=5)`), then exits
- Rules are read once at startup; editing them requires a restart
- Packet capture generally requires root/admin privileges

## Project structure

```text
SecureWall/
├── config/
│   ├── blocked_ips.txt     # source IPs to flag as BLOCK
│   └── rules.txt           # destination ports to flag as BLOCK
├── firewall/
│   ├── logger.py           # writes decisions to logs/firewall.log
│   ├── packet.py           # Packet data class
│   ├── rules.py            # RuleEngine: ALLOW/BLOCK decisions
│   └── sniffer.py          # Scapy sniffing + per-packet logic
├── logs/                   # firewall.log is written here at runtime
├── main.py                 # entry point
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/vyshnavbalakrishnan17-png/SecureWall.git
cd SecureWall
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Packet capture usually needs elevated privileges:

```bash
sudo python main.py      # Linux / macOS
# On Windows, run from an elevated (Administrator) shell
```

The sniffer processes 5 packets, prints each one with its decision, appends them to
`logs/firewall.log`, then exits.

## Configuration

- `config/rules.txt` — one destination port per line to flag as `BLOCK`
- `config/blocked_ips.txt` — one source IP per line to flag as `BLOCK`

## Requirements

- Python 3
- [Scapy](https://scapy.net/)
- Permission to capture packets
