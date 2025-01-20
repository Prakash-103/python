from paramiko import client    # Import the paramiko library

from getpass import getpass   # Import the getpass library

import time    # import the time for 

hostname = '192.168.107.137' 

username = input("Enter the username:")

if not username:
    username = "admin"
print(f"the default username will be {username}.")

password = getpass(f"Enter the password for the {username} to log in: ") or 'pass1234'


ssh_client=client.SSHClient()       # creating the connection for the ssh client
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)    # adding the policy for the missing host key for auto known host policy

print(dir(ssh_client))  # print the dir of the ssh client

ssh_client.connect(hostname= hostname,
                   port= 22,
                       username= username,
                           password= password,
                           look_for_keys= False,
                           allow_agent= False)
# creating the connection between the target host

print(" connection is connected sucessfully")

device_connection= ssh_client.invoke_shell()          # to access the shell to execute the commands
device_connection.send(" terminal length 0 \n")       # send the command to the device to get the output in one line            
device_connection.send(" sh run \n")        
time.sleep(5)       # to wait for 5 seconds to get the output       

output=device_connection.recv(65535).decode("utf-8")  # recv will be in bytes the command to recive the output from the device

print (output)
ssh_client.close()              # close the ssh connection 
