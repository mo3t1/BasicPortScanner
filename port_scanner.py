import socket

def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # 0.5 seconds timeout for each port
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan aborted by user.")
            return
        except socket.error:
            print("\nCouldn't connect to server.")
            return
    
    if open_ports:
        print("\nOpen ports:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("\nNo open ports found in the given range.")

def valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        num = int(item)
        if num < 0 or num > 255:
            return False
    return True

def main():
    ip = input("Enter the IP address to scan: ").strip()
    if not valid_ip(ip):
        print("Invalid IP address format.")
        return

    try:
        start_port = int(input("Enter start port: ").strip())
        end_port = int(input("Enter end port: ").strip())
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("Invalid port range.")
            return
    except ValueError:
        print("Ports must be numbers.")
        return

    scan_ports(ip, start_port, end_port)

if __name__ == "__main__":
    main()

