from scapy.all import sniff

# Define the packet handler function
def packet_handler(packet):
    print(packet.show())

# Start sniffing the network
print("Sniffing network... Press CTRL+C to stop.")
sniff(prn=packet_handler, store=0)
