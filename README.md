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

- Python 3
- Scapy 2.7.01
- Kali Linux
- Ubuntu Linux
- VirtualBox
- VirtualBox Host-Only Networking

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
```

If Scapy is not installed, use Kali's package manager:

    sudo apt update
    sudo apt install -y python3-scapy

Verify the installation:

    python3 -c "import scapy; print(scapy.__version__)"

The project was tested successfully with Scapy version 2.7.01.

## Running the Sniffer

Navigate to the project directory:

    cd ~/CodeAlpha/Task1_Network_Sniffer

Run the network sniffer with root privileges:

    sudo python3 network_sniffer.py

The program captures traffic on the eth0 interface. Press CTRL+C to stop the packet capture.


## Packet Information Captured

For each captured IP packet, the program records:

- Timestamp
- Source IP address
- Destination IP address
- Network protocol
- TCP or UDP source and destination ports
- ICMP type
- Packet size
- Payload length
- Safe printable payload preview

## Supported Protocols

| Protocol | Information Identified |
|---|---|
| TCP | Source port, destination port and payload |
| UDP | Source port, destination port and payload |
| ICMP | ICMP type and payload |
| Other | Other IP-based protocols |

## Packet Logging

Captured packet information is automatically saved to packet_capture.log.

## Packet Statistics

When the sniffer is stopped with CTRL+C, it displays the total number of packets and the number of TCP, UDP, ICMP and other packets captured.

## Payload Analysis

The program checks whether a packet contains a Raw payload.

When payload data is available, the program:

1. Extracts the payload bytes.
2. Calculates the payload length.
3. Converts printable ASCII characters into readable text.
4. Replaces non-printable characters with a period.
5. Displays a maximum of 50 characters as a safe preview.

This provides basic visibility into packet contents without attempting to reconstruct complete application-layer sessions.

## Testing

The sniffer was tested using Kali Linux and Ubuntu Linux connected through a VirtualBox Host-Only network.

Test traffic was generated from Ubuntu using:

    ping -c 5 192.168.56.102

## Test Results

One documented test run captured 30 packets:

| Protocol | Packets Captured |
|---|---:|
| TCP | 18 |
| UDP | 2 |
| ICMP | 10 |
| Other | 0 |
| Total | 30 |

The test successfully demonstrated source and destination identification, protocol detection, port identification, packet size measurement, payload analysis, logging and packet statistics.

## Security and Ethical Considerations

This project was developed and tested in an isolated laboratory environment using systems under authorized control.

Network sniffing should only be performed on systems and networks where permission has been granted.

## Limitations

- Monitors only the configured network interface.
- Does not decrypt encrypted traffic.
- Does not reconstruct complete network sessions.
- Does not perform deep protocol analysis.
- Does not provide a graphical user interface.
- Does not automatically classify malicious traffic.
- Does not provide automated intrusion response.

## Future Improvements

- Add command-line options for selecting the network interface.
- Add protocol filters.
- Add packet capture duration options.
- Export captured data to CSV or JSON.
- Add PCAP file support.
- Add additional protocol detection.
- Develop a graphical interface.
- Integrate basic threat detection capabilities.

## Conclusion

The CodeAlpha Task 1 Network Sniffer demonstrates fundamental network packet capture and analysis using Python and Scapy. The project captures live traffic, identifies common protocols, displays source and destination information, analyzes packet sizes and payloads, records captured traffic in a log file, and generates protocol statistics.