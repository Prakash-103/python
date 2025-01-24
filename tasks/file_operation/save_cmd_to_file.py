from paramiko import client,ssh_exception
import time
import sys
import socket
import traceback
import datetime

hostname= '192.168.107.137'

username= "admin1"
password= "pass123"

juno_cmd=['show configuration | display set | no-more', ' show interfaces terse | no more','show lldp | no more']


def exe_commands(hostname,command):
    try:
        print (f"Connecting to {hostname}...")
        now= datetime.datetime.now().replace(microsecond=0)         # for live time stamp without microseconds   
        current_conf_file= f'{now}_{hostname}'                      # for dynamic file name

        ssh=client.SSHClient()
        ssh.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh.connect(hostname=hostname,
                    port=22,
                    username=username,
                    password=password,
                    look_for_keys=False,allow_agent=False)
        print(f' connected to the {hostname}')

        int_config=ssh.invoke_shell() #invoke shell 

        with open(current_conf_file,'w') as conf:           # open the file to write 
            for cmd in command:             # for executing comands

                    int_config.send(f" {cmd} \n")
                    time.sleep(1)
                    output=int_config.recv(65535).decode('utf-8')
                    conf.write(output)                              # store the precheck output in the file
                    print(output)
                    
            int_config.send(" show run \n")                # for sh run commmands
            time.sleep(1)                      
            output=int_config.recv(65535).decode('utf-8')
            conf.write(output)                              # store the run command output in the file
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

    

exe_commands( hostname,juno_cmd)

