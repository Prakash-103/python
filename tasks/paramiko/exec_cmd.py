from paramiko import RSAKey # type: ignore
import getpass

hostname= "192.168.107.137"
username=input("\U0001F601 Enter the username: ") or "admin1"
password=getpass.getpass("Enter the password: ") or "pass123"

juno_cmd=[ ' show interfaces terse ','sh lldp']
#key_file=RSAKey.from_private_key_file(filename='/home/root1/.ssh/id_rsa')
def exe_commands(hostname,command):

    print (f"Connecting to {hostname}...")

    ssh=paramiko.SSHClient() # type: ignore
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # type: ignore
    ssh.connect(hostname=hostname,
                port=22,
                username=username,
                password=password,
                look_for_keys=True,allow_agent=True,
                pkey=key_file)
    print(f' connected to the {hostname}')
    for cmd in command:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print (f"\n {'='*10}  output for {cmd} {'='*10} \n\n ")
        print(stdout.read().decode())   
        err=stderr.read().decode()
        if err:
            print( f"  this erroroccured {err}")

    
    ssh.close()
    print(f" ssh {hostname} connection closed")

    






exe_commands( hostname,juno_cmd)

