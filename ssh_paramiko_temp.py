# from paramiko import client
# from getpass import getpass

# hostname = '192.168.107.137'

# username = input("Enter the username:")
# if not username:
#     username = "admin"
# print(f"the default username will be {username}.")

# password = getpass(f"Enter the password for the {username} to log in: ") or 'pass1234'


ssh_client=client.SSHClient()

print(dir(ssh_client))