from paramiko import client,ssh_exception,rsakey
import paramiko.util
import time
import sys
import socket
import traceback

paramiko.util.log_to_file(filename='/home/root1/Python_for_networking/python/files/error_hand.log',level='DEBUG')

hostname= '192.168.107.137'

username= "admin1"
password= "pass123"

juno_cmd=['show configuration | display set | no-more', ' show interfaces terse | no more','show lldp | no more']
key_file=rsakey.RSAKey.from_private_key_file(filename='/home/root1/.ssh/id_rsa.pub')
def exe_commands(hostname,command):
    try:
        print (f"Connecting to {hostname}...")

        ssh=client.SSHClient()
        ssh.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh.connect(hostname=hostname,
                    port=22,
                    username=username,
                    password=password,
                    look_for_keys=True,allow_agent=True,
                    pkey=key_file,
                    disabled_algorithms=dict(pub_keys= ['rsa-sha-512','rsa-sha-256']))
        print(f' connected to the {hostname}')
        for cmd in command:
            try:    
                int_config=ssh.invoke_shell()
                int_config.send(f" {cmd} \n")
                time.sleep(1)
                output=int_config.recv(65535).decode('utf-8')
                print(output)
            except:
                print(f"Error in  executing command {cmd}")

        
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

