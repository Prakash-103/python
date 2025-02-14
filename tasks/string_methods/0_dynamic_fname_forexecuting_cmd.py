from paramiko import client,ssh_exception
import time
import sys
import socket
import traceback
import datetime

hostname= '192.168.107.137'

username= "admin1"
password= "pass123"

def cmd_file(command_file):
    with open(command_file,'r') as file1:
        config_cmds=file1.readlines()
        return(config_cmds)
    #print (config_cmds)

def exe_command_files(hostname,command_file,username=username,password=password):
    try:
        print (f"Connecting to {hostname}...")
        now= datetime.datetime.now().replace(microsecond=0)            
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
        config_file=cmd_file(command_file)
        for cmd in enumerate(config_file,start=1):          # code to auto organize the structure
            file_name=f'{str(now).replace(" ",":")}_{str(cmd[0]).zfill(2)}_{str(cmd[1]).replace(" ","_").strip()}.json' # converting the exch f-int as str to manupulate it and gives the output in diff file 
            
            with open(file_name,'w') as file1:     # code for the file name to be open and run the cmd
                int_config.send(f" {str(cmd[1])} ")        
                time.sleep(1)
                output=int_config.recv(65535).decode('utf-8')
                file1.write(output)                              
                return(output)

        ssh.close()
        return(f" ssh {hostname} connection closed")



    except socket.gaierror:
        return(f" the  {hostname} is not reachable or not valid")

    except  ssh_exception.NoValidConnectionsError:
        return(f" Enter the valid hostname...")


    except ssh_exception.AuthenticationException:
        return(f" authentication failed for {hostname} ")


    except:
        traceback.print_exception(*sys.exc_info())
        return(sys.exc_info())
    

    

#exe_command_files( hostname,config_cmds,password,username)

print(cmd_file('sh_config.txt'))

command_file= "commands.txt" 

print(exe_command_files( hostname,command_file,password,username))