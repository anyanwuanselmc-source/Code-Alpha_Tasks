#!/usr/bin/env python3

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


LOG_FILE = "packet_capture.log"


def get_payload(packet):
    """Extract a safe printable preview of the packet payload."""

    if Raw not in packet:
        return "-", 0

    payload = bytes(packet[Raw].load)
    payload_length = len(payload)

    # Keep only printable characters for safe terminal display
    preview = "".join(
        chr(byte) if 32 <= byte <= 126 else "."
        for byte in payload[:50]
    )

    return preview, payload_length


def packet_callback(packet):
    """Analyze and display captured IP packets."""

    if IP not in packet:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)

    # Identify protocol and ports
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

    payload_preview, payload_length = get_payload(packet)

    output = (
        f"[{timestamp}] "
        f"{source_ip} -> {destination_ip} | "
        f"{protocol} | "
        f"{details} | "
        f"Size: {packet_size} bytes | "
        f"Payload: {payload_length} bytes | "
        f"Data: {payload_preview}"
    )

    print(output)

    # Save captured information to the log file
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(output + "\n")


def main():
    print("=" * 100)
    print("                 CodeAlpha - Basic Network Sniffer v2")
    print("=" * 100)
    print("Interface : eth0")
    print("Log file  : packet_capture.log")
    print("Status    : Capturing packets...")
    print("Press CTRL+C to stop.")
    print("=" * 100)

    try:
        sniff(
            iface="eth0",
            prn=packet_callback,
            store=False
        )

    except KeyboardInterrupt:
        print("\n\n[+] Packet capture stopped.")
        print("[+] Network sniffer terminated.")
        print(f"[+] Captured packet information saved to {LOG_FILE}")


if __name__ == "__main__":
    main()
