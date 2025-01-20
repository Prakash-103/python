from paramiko import client
import getpass

hostname = '192.168.107.137'

username = input("Enter the username:")
if not username:
    username = "admin"
print(f"the default username will be {username}.")

password = getpass.getpass(f"Enter the password for the {username} to log in: ") or 'admin'
