from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto

        if TCP in packet:
            print(f"[TCP] {src} → {dst} | Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"[UDP] {src} → {dst} | Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print(f"[ICMP] {src} → {dst}")

        if packet[IP].payload:
            payload = bytes(packet[IP].payload)
            print(f"  Payload: {payload[:50]}")

print("Starting Network Sniffer... Press Ctrl+C to stop")
sniff(prn=packet_callback, count=50, store=0)