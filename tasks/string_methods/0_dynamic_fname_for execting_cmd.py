from paramiko import client,ssh_exception
import time
import sys
import socket
import traceback
import datetime

hostname= '192.168.107.137'
username= "admin1"
password= "pass123"


with open('sh_config.txt','r') as file1:
     config_cmds=file1.readlines()

print (config_cmds)

def exe_commands(hostname,command):
    try:
        print (f"Connecting to {hostname}...")
        now= datetime.datetime.now().replace(microsecond=0)            
        #current_conf_file= f'{now}_{hostname}'                     

        ssh=client.SSHClient()
        ssh.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh.connect(hostname=hostname,
                    port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,allow_agent=False)
        print(f' connected to the {hostname}')

        int_config=ssh.invoke_shell() #invoke shell 

        #with open(current_conf_file,'w') as conf_file:           
        
        for cmd in enumerate(command,start=1):          # code to auto organize the structure
            file_name=f'{str(now).replace(" ",":")}_{str(cmd[0]).zfill(2)}_{str(cmd[1]).replace(" ","_").strip()}.json' # converting the exch f-int as str to manupulate it and gives the output in diff file 
            
            with open(file_name,'w') as file1:     # code for the file name to be open and run the cmd
                int_config.send(f" {cmd[1]} ")        
                time.sleep(1)
                output=int_config.recv(65535).decode('utf-8')
                file1.write(output)                              
                print(output)

        ssh.close()
        print(f" ssh {hostname} connection closed")



    except socket.gaierror:
        print (f" the  {hostname} is not reachable or not valid")

    except  ssh_exception.NoValidConnectionsError:
        print(f" Enter the valid hostname...")


    except ssh_exception.AuthenticationException:
        print (f" authentication failed for {hostname} ")


    except:
        print(f" unable to connect to {hostname}")
        print(sys.exc_info())
        traceback.print_exception(*sys.exc_info())

    

exe_commands( hostname,config_cmds)

