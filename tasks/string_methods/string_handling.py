username='admin123'
passwrd='     Sdf  12 $DE  123'
# print(username.capitalize()) # Output: Admin123 change the first letter capital
# print(passwrd.casefold()) # change to the lower case
# print(username.upper()) # change to upper case
# print(passwrd.rsplit('$')) # splits accrging to the condition
# print(passwrd.strip())# removeş the before and after whitespaces in the variable
# print (passwrd.replace(" ","")) # it removes the space inbetween the character.

# user_input=input(' Enter the user name :').upper().strip().replace(" ","")

# if user_input == username:
#     print (f' the {user_input} name is valid !!!')
# else:
#     print( ' enter the valid user name ')       


####################################################################################################################

# # string formating

# print(' the username is {0} \n the password is {1}'.format(username,passwrd.replace(" ",""))) # old method
# print(f' the username is {username} \n the password is {passwrd.replace(" ","")}') # new method

# ###################################################################################################################



# # find

# print(username.find('9')) # in this method the output is -1 then the value is not present on the variable

# print(username.index("3")) # in this methos is throws the error while value is not present

# ###################################################################################################################

# # is decimal


# print(passwrd.isdecimal())
# print(passwrd.isalnum())
# print(passwrd.isidentifier()) # is verifies the a-z A-Z 0-9 _  are present in the variable should not start with number
# print(passwrd.isascii())
# print(passwrd.isprintable()) # it verifies the the variable is printable or not it becomes false when \n \t else present in the file or variable


#######################################################################################################################

# join is used to ion the list using the special characters

# list1= ['cisco','ios','v21.1']

# print('-'.join(list1))
# print('__'.join(list1))

# ####################################################################################################################

# # ljust is used to display the values is the ordered way

# print('ios'.ljust(20),'v21')
# print('juniperios'.ljust(20),'v22')
# print('sonicios'.ljust(20),'v23')
# print('ios'.ljust(20),'v24')

# ###############################################################################################################

# # maketrans is ues to make the particuler changes the maketran word will be  in the same length of the string

# msg='hi there, \n how are you'
# tran=str.maketrans('hi','He')
# print(msg.translate(tran))

# #############################################################################################################

# # partition it makes the partion based nthe input we given in the string

# print(msg.partition('how'))

# ##############################################################################################################

# #replace will replace the word accorcding to the input we given

# print(msg.replace("hi", 'hello'))

# ###############################################################################################################

# # splitlines it useds to display the list of lines in the array

# print(msg.splitlines())
# print(msg.splitlines(True))         # includes the  \n

# ###########################################################################################################

# # zfill or zero_fill it defines the char and fill the remaining char by zero's

# print(username.zfill(10))

# ###########################################################################################################

# # translate can be match by unicode

# trans={46: 33}   # it matches the unicode of   .  and !

# print('hithere....'.translate(trans))

##############################################################################################################






