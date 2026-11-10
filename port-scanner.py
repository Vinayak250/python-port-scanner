
import socket

target = input("Enter target IP address: ")

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

open_ports = []

print("\nScanning", target, "...")

for port in range(start_port, end_port + 1):

    s = socket.socket()
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")
        open_ports.append(port)

    s.close()

print("\nScan complete!")

if len(open_ports) > 0:
    print("Open ports:", open_ports)
    print("Total open ports:", len(open_ports))
else:
    print("No open ports found.")
