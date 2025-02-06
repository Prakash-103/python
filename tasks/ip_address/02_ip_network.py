import ipaddress

ip=ipaddress.ip_network('192.168.0.0/24')


print(type(ip))
print(ip.network_address) # network address
print(ip.broadcast_address) # broadcast ip
print(ip.hostmask)  # hostmask
print(ip.max_prefixlen) # number of bits in the prefix
print(ip.num_addresses) # number of available address
print(ip.with_prefixlen) # print ip with prefix   

# for data in ip:                 one way
#     print(data)

# for ip1 in ip.hosts():          other way
#     print(ip1)


# print(ip.overlaps(ipaddress.ip_network('192.168.1.5'))) # check wether ht e ip in the samenetwork

# ip_add1=ipaddress.ip_address('192.168.0.8')
# print(ip_add1 in ip)

new_exclude=ipaddress.ip_network('192.168.0.8')

l1= ip.address_exclude(new_exclude) 

for ip in l1:
    print(ip)