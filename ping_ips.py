import subprocess

def ping_ip(ip):
    #ping -c 1 <ip>  # (Linux/macOS)
    result = subprocess.run(['ping','-n','1',ip],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    return result.returncode == 0


def check_ips(ip_list):
    for ip in ip_list:
        print(ip)
        if ping_ip(ip):
            print(" the given ip is reacahble----", ip)
        else:
            print(" not reachble")


if __name__ == '__main__':
      # List of IPs to check
    ips_to_check = [
        "8.8.8.8",       # Google DNS
        "192.168.1.1",   # Common router IP
        "10.255.255.1",  # Likely unreachable
        "127.0.0.1"      # Loopback
    ]
    check_ips(ips_to_check)