username='admin123'
passwrd='     Sdf  12 $DE  123'
print(username.capitalize()) # Output: Admin123 change the first letter capital
print(passwrd.casefold()) # change to the lower case
print(username.upper()) # change to upper case
print(passwrd.rsplit('$')) # splits accrging to the condition
print(passwrd.strip())# removeş the before and after whitespaces in the variable
print (passwrd.replace(" ","")) # it removes the space inbetween the character.

user_input=input(' Enter the user name :').upper().strip().replace(" ","")

if user_input == username:
    print (f' the {user_input} name is valid !!!')
else:
    print( ' enter the valid user name ')       


####################################################################################################################