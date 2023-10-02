import ipaddress

ip = "188.87.101.2108"

try:
    ipaddress.ip_address(ip)

    split_ip = "\n".join(ip.split('.'))
    print(split_ip)   

except:
    print("ip is invalid")


