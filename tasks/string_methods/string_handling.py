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

# string formating

print(' the username is {0} \n the password is {1}'.format(username,passwrd.replace(" ",""))) # old method
print(f' the username is {username} \n the password is {passwrd.replace(" ","")}') # new method

###################################################################################################################



# find

print(username.find('9')) # in this method the output is -1 then the value is not present on the variable

print(username.index("3")) # in this methos is throws the error while value is not present

###################################################################################################################

# is decimal


print(passwrd.isdecimal())
print(passwrd.isalnum())
print(passwrd.isidentifier()) # is verifies the a-z A-Z 0-9 _  are present in the variable should not start with number
print(passwrd.isascii())
print(passwrd.isprintable()) # it verifies the the variable is printable or not it becomes false when \n \t else present in the file or variable


#######################################################################################################################

