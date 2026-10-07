#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime


def packet_callback(packet):
    """Analyze and display captured IP packets."""

    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)

    # Identify protocol
    if TCP in packet:
        protocol = "TCP"
        details = f"{packet[TCP].sport} -> {packet[TCP].dport}"

    elif UDP in packet:
        protocol = "UDP"
        details = f"{packet[UDP].sport} -> {packet[UDP].dport}"

    elif ICMP in packet:
        protocol = "ICMP"
        details = f"Type={packet[ICMP].type}"

    else:
        protocol = "Other"
        details = "-"

    print(
        f"[{timestamp}] "
        f"{source_ip} -> {destination_ip} | "
        f"{protocol} | "
        f"{details} | "
        f"{packet_size} bytes"
    )


def main():
    print("=" * 80)
    print("              CodeAlpha - Basic Network Sniffer")
    print("=" * 80)
    print("Interface : eth0")
    print("Status    : Capturing packets...")
    print("Press CTRL+C to stop.")
    print("=" * 80)

    try:
        sniff(
            iface="eth0",
            prn=packet_callback,
            store=False
        )

    except KeyboardInterrupt:
        print("\n[+] Packet capture stopped.")
        print("[+] Network sniffer terminated.")


if __name__ == "__main__":
    main()
