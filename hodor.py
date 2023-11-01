import socket
from time import sleep
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # set timeout to 1 second
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Port {} is open".format(port))
        else:
            print("Port {} is closed".format(port))
    except socket.error:
        print("Can't connect to host")

def scan_range(ip, start_port, end_port):
    for port in range(start_port, end_port+1):
        scan_port(ip, port)
        sleep(1) # delay between scans
        print("Scanning port {}".format(port))
if __name__ == "__main__":
    ip = input("Enter IP address: ")
    start_port = int(input("Starting port: "))
    end_port = int(input("Ending port: "))
    scan_range(ip, start_port, end_port)
