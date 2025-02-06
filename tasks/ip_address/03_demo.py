import ipaddress


net_list=[]

while True:
    try:
        ip = input("Enter IP address/list/exit: ")

        if ip=='exit':
            print('exiting the program')
            break
            
        if ip=='list':
            print(net_list)
            continue
        else:
            ip_input=ipaddress.ip_address(ip)

        lan_network=ipaddress.ip_network('192.168.0.0/24') 

        if ip_input not in net_list:
            if ip_input in lan_network:
                net_list.append(ip)
            else:
                print(f"{ip_input} is not in the network")
        else:
            print('Already exist!!!')
    
    except ValueError:
        print(f"Invalid input")