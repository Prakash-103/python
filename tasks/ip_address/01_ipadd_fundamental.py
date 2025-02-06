import ipaddress


ip=ipaddress.ip_address('192.168.0.12')

print(type(ip))     # type of the ip
print(type(ip.compressed)) # convert of the ip to string
print(type(ip.exploded)) # convert of the ip to string
print(ip.max_prefixlen) ###  prints the length og the longest possible prefix its 32-- ipv4 128-- ipv6
print(ip.is_global)
print(ip.is_private)
print(ip.is_loopback)
print(ip.is_link_local)
print(ip.version)
print(ip.is_multicast)
print(ip.is_reserved)       
print(ip.is_unspecified)        

try:
    ip1=ipaddress.ip_address(input(" enter ip:"))
    print(ip1)

except:
    print('enter the valid ip')