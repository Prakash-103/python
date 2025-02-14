import re

with open('comparison_file.txt','r') as in_file:
    data=in_file.read()

# print(check_file)
pattern1= r"\sparamiko"   # match the paramiko only
pattern2= r"p.+,*-paramiko_(\d\S+)"    # match teh paramiko till the last wordof the sentence and group the version value as group(1)
                                            

# print(pattern1)
re_out=re.search(pattern2,check_file)
# print(re_out)
if re_out:
    print('match found')
    print(re_out)       # prints the value expect the group(1)
    print(re_out.group(0)) # prints the every element matches
    print(re_out.group(1)) # prints the group(1) value  
    print(f" {'The version of paramiko'.rjust(18)} : {re_out.group(1)}")
else:
    print('match not found')

####################################################################################################################

###   compile method @ this create the pattern as object 

my_pattern=re.compile(r"p.+,*-paramiko_(\w.+)") #matches the \w. matchs the a-z,A-Z,0-9 . represent the . then + match till end in same order

matches=my_pattern.search(string=data)
print(matches)
print(matches.group(0))
# print(matches.group(1))
#####################################################################################
############        find all

my_pattern= re.compile(r"s.h"  ) # match the paramiko only


file=my_pattern.findall(string=data)  # matches allvalues in the file

print(file)

######################################################################################

##########      finditer

result=my_pattern.finditer(string=data) # matches allvalues in the file but we want to print by itering or by for() it

print(result)

for iter in result:
    print(iter)
    print(iter.group())        
    print(iter.span())


###################################################################################################

######      user input validation

os_version=input(" Enter the OS version:").casefold()
my_pattern1=re.compile(r'^cisco.+23.4.02$') # matches the CISCO___________23.4.02   ^ starts with  $ endswith
match=my_pattern1.search(os_version)

if match:
    print('the value match:',match)
else:
    print ('no match')

###########################################################################################

#############  email validation

str=''
ptrn=re.compile(r'')
result=ptrn.finditer(str)
for iter in result:                     
    print(iter)



##################################################################################################

#### multiline pattern matching 
os_version=input(" Enter the OS version:").casefold()
print(re.findall(pattern=r'\Acisco.+23.4.02\Z',string='osversion',flags=re.MULTILINE))
#\A represents the only the starting line  || \z represents the only the ending line
if match:
    print('the value match:',match)
else:
    print ('no match')

##################################################################################################
#######  \b  \B
pattern2=(r'\bcisco') # matches only at the begining of the string
pattern4=(r'cisco\b') # matches only at the end of the string
pattern3=(r'\Bcisco') # matches only at the middle of the string

#######################################################################################################

########            {m,n}

pattern1=(r'cisco{2,5}')  # it iter the occurance of cisco 2 to 5 times
match=re.search(pattern1,'ciscooooo')       
print(match)

######################################################################################################
##########  \*\n
pattern1=(r'\*\n') 

####################################################################################################3

#################### ignore case re.I

print(re.search('hello','Hello',re.I))

#################################################################################################33
#       dotall

print(re.search('hello.hello','Hello\nhello',flags=re.DOTALL | re.IGNORECASE))

################################################################################################
pattern1=re.compile(r'abcd1234qwe')
print(re.match('abcd',pattern1))
print(re.search('1234qwe',pattern1))
print(re.fullmatch(abcd1234qwe,pattern1))

################################################################################################

#### sub

print(re.sub(r'abc',r'ABC',pattern1))  # replace the values as per the expense
print(re.subn(r'abc',r'ABC',pattern1)) # includes no words replaces


