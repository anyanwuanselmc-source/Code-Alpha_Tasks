# CodeAlpha Task 1 — Basic Network Sniffer

## Project Overview

This project implements a basic network packet sniffer in Python using the Scapy library.

The application captures live network traffic from a specified network interface, analyzes packet information, identifies common network protocols, extracts source and destination information, analyzes available payload data, and records captured traffic in a log file.

This project was developed as part of the CodeAlpha Cyber Security Internship.

## Objectives

The objectives of this project are to:

- Capture live network packets.
- Identify common network protocols.
- Display source and destination IP addresses.
- Display TCP and UDP source and destination ports.
- Analyze packet sizes and payload lengths.
- Display a safe printable preview of packet payloads.
- Record captured packet information in a log file.
- Generate protocol-based packet statistics.
- Develop practical understanding of network traffic and data flow.

## Technologies Used

- **Python 3**
- **Scapy 2.7.01**
- **Kali Linux**
- **VirtualBox**
- **Linux networking**
- **VirtualBox Host-Only networking**

## Project Structure

```text
Task1_Network_Sniffer/
│
├── network_sniffer.py
├── network_sniffer_v1.py
├── network_sniffer_v2.py
├── network_sniffer_v3.py
├── packet_capture.log
├── requirements.txt
└── README.md
```

## Network Lab

The network sniffer was tested in an isolated **VirtualBox Host-Only network** to provide a controlled environment for packet capture and analysis.

| System | Interface | IP Address | Role |
|---|---|---|---|
| Kali Linux | eth0 | 192.168.56.102 | Packet-sniffing system |
| Ubuntu Linux | enp0s8 | 192.168.56.105 | Test traffic generator |

The **Kali Linux** machine was used to capture and analyze network packets, while the **Ubuntu Linux** machine generated controlled test traffic such as ICMP ping requests and responses.

This isolated laboratory environment was used to ensure that packet capture and analysis were performed only on authorized systems.

## Installation

### Kali Linux

Scapy is required to run the network sniffer.

Check whether Scapy is installed:

```bash
python3 -c "import scapy; print(scapy.__version__)"


If Scapy is not installed, use Kali's package manager:

```bash
sudo apt update
sudo apt install -y python3-scapy
