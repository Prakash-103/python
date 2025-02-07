import sys

path=sys.path.append('/home/root1/Python_for_networking/python/tasks/paramiko')

# path=sys.path.insert( 0 ,'/home/root1/Python_for_networking/python/tasks/paramiko')  #----- insert by giving the priority
# print(sys.path)

from pass_gen import users_cmd,user_cmd
from def_ssh import exe_commands

dict1=[{'name':'admin','privilage':15},{'name':'admin3','privilage':12},{'name':'prakash','privilage':13}]

print(user_cmd('prakash',10))
print(users_cmd(*dict1))

exe_commands('192.168.0.121',user_cmd('prakash',10))

