import socket
from datetime import datetime

target = input("Enter the target IP address: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))

print(f"Scanning ports from {start_port} to {end_port} on {target}...")

start_time = datetime.now()

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    
    s.close()

end_time = datetime.now()

print(f"Scan completed in {end_time - start_time}")
