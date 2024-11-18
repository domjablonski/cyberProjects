from scapy.all import sniff

def packet_handler(packet):
    print(packet.show())

print("Sniffing network... Press CTRL+C to stop.")
sniff(prn=packet_handler, store=0)
