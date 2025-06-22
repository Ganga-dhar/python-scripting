import ipaddress

def ip_address_check(ip_add):
    try:
        ip = ipaddress.ip_address(ip_add)
        print("This is a valid IP:", ip)

        if isinstance(ip, ipaddress.IPv4Address):
            print("This is a valid IPv4 address.")
        elif isinstance(ip, ipaddress.IPv6Address):
            print("This is a valid IPv6 address.")
    except ValueError:
        print("This is not a valid IP address.")

if __name__ == '__main__':
    ip = input("enter the ip address")
    ip_address_check(ip)
