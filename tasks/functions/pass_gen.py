import string
import random

def user_cmd(user,priv):
    password= ''.join(random.choices(string.ascii_letters + string.digits,k=8 ))  # it join the values in the list and add digits in the password values
    cmd_line= f" username {user} privilage {priv} secret {password}\n"
        
    return cmd_line


def users_cmd(*args):
    aut_list=[]
    for value in args:
        password= ''.join(random.choices(string.ascii_letters + string.digits,k=8 ))  # it join the values in the list and add digits in the password values
        cmd_line= f" username {value['name']} privilage {value['privilage']} secret {password}\n"
        aut_list.append(cmd_line)
    return aut_list




###  this condition means, if the main files is run directly it will execute the function    
if __name__ == '__main__': 
    print(__name__)
    dict1=[{'name':'admin','privilage':15},{'name':'admin3','privilage':12},{'name':'prakash','privilage':13}]
    print(user_cmd('admin',15))
    print(users_cmd(*dict1))

