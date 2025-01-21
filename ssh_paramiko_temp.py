from paramiko import client    # Import the paramiko library

from getpass import getpass   # Import the getpass library

import time    # import the time for 

hostname = '192.168.107.137' 

username = input("Enter the username:")

if not username:
    username = "admin1"
print(f"the default username will be {username}.")

password = getpass(f"Enter the password for the {username} to log in: ") or 'pass123'


ssh_client=client.SSHClient()       # creating the connection for the ssh client
#ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)    # adding the policy for the missing host key for auto known host policy
#ssh_client.load_system_host_keys() # loading the system host keys  
#ssh_client.load_host_keys( filename='/home/root1/.ssh/known_hosts') # loading the host keys from the file

ssh_client.set_missing_host_key_policy(client.WarningPolicy) # adding the policy for the missing host key for warning policy
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
device_connection.send(" show configuration | display set | no-more \n")           
device_connection.send(" sh interfaces terse \n")        
time.sleep(5)       # to wait for 5 seconds to get the output       

output=device_connection.recv(65535).decode("utf-8")  # recv will be in bytes the command to recive the output from the device

print (output)
# ssh_client.close()              # close the ssh connection 
