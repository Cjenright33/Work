import socket

def port_scanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except:
        print("Could not connect to the host")

url = input("Enter the URL to scan: ")

try:
    host = socket.gethostbyname(url)
except socket.gaierror:
    print("Host not found.")
    exit()

start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

for port in range(start_port, end_port + 1):
    port_scanner(host, port)