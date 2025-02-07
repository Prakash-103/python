import string
import random


# def pass_generate(admin,privilege):
# # password=random.choice(string.ascii_letters )  # .... it provides only the one character                                
# # password=random.choices(string.ascii_letters,k=8 ) # it provides 8 characters and it contains all the elements in the array
#     password= ''.join(random.choices(string.ascii_letters + string.digits,k=8 ))  # it join the values in the list and add digits in the password values
#     return f' username {admin} privilage {privilege} secret {password}\n'


#print(pass_generate('admin1',15))  # it will print the password for the admin with super

# while True:                 # try looping to initiate user to enter details
#     user=input('Enter the username/exit:')
    
#     if user=='exit':
#         print('process closed....')
#         break

#     access=int(input('enter the privilage level:'))
#     with open('test.txt','a') as file:
#         file.write(pass_generate(user,access)) 

#########################################################################################

# lis1=['admin',12]

# print(pass_generate(*lis1))
# print(pass_generate(*['admin3',13]))
# print(pass_generate(*[lis1[0],lis1[1]]))

# ##########################################################################################
# dict1={'admin':'ad123','privilege':16}

# print(pass_generate(**dict1))

# ##################################################################################

# list1=['sh version','sh ip int brief','sh run']

# dict_1={'location':'chennai','branch':'egmore'}

# def pass_generate(admin,privilege,*args,**kwargs):
#     password= ''.join(random.choices(string.ascii_letters + string.digits,k=8 ))  # it join the values in the list and add digits in the password values
#     print( f' username {admin} privilage {privilege} secret {password}\n')
    
#     for i in args:
#         print(i)

#     for data in kwargs:
#         print(data,kwargs[data])            

# pass_generate('adnmin12',15,list1,dict_1)

    
# for i in list1:
#     print(i)

# for data in dict_1:
#     print(data,dict_1[data])  

# for data in dict_1.items():
#     print(data)          
########################################################################################################

#  type 3


dict1=[{'name':'admin','privilage':15},{'name':'admin3','privilage':12},{'name':'prakash','privilage':13}]

# print(type(dict_1))
# for value in dict_1:
#     print(value['name'])

def pass_generate(*args):
    aut_list=[]
    for value in args:
        password= ''.join(random.choices(string.ascii_letters + string.digits,k=8 ))  # it join the values in the list and add digits in the password values

        cmd_line= f" username {value['name']} privilage {value['privilage']} secret {password}\n"
        aut_list.append(cmd_line)
    return aut_list

pass_generate(*dict1)