import paramiko 
import time
import getpass

hostname= input(" Enter the valid hostname: ")

username=input("\U0001F601 Enter the username: ") or "admin1"
password=getpass.getpass("Enter the password: ") or "pass123"

juno_cmd=['show configuration | display set | no-more', ' show interfaces terse | no more','show lldp | no more']

def exe_commands(hostname,command):

    print (f"Connecting to {hostname}...")

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,
                port=22,
                username=username,
                password=password,
                look_for_keys=False,allow_agent=False)
    print(f' connected to the {hostname}')
    for cmd in command:
        int_config=ssh.invoke_shell()
        int_config.send(f" {cmd} \n")
        time.sleep(1)
        output=int_config.recv(65535).decode('utf-8')
        print(output)
    
    ssh.close()
    print(f" ssh {hostname} connection closed")

    






if __name__ == "__main__":  # the below command runs only this file executes....
    exe_commands( hostname,juno_cmd)