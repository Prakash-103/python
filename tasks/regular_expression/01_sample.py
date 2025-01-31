st=r'\nhi\tthere\n'  # re must be in the raw string
print(st)
print(type(st)) #allways be the str type

# href: regex101.com
st='[cC]isco' #re must be in the raw string
st='[Cc]i*sco' # re * must 0 or more iterations in the str 
st='[Cc]i+sco' # re + must 1 or more iterations in the str  
st='[Cc]i?sco' # re ? must 0 or 1 iteration in the str  
st='[Cc]i{2}sco' # re {2} must 2 iterations
st='^[Cc]i*sco' # re ^ must start with the str
st='[Cc]i*sco$' # re $ must end with the str    
st='[Cc]i*.co' # re . must any char in the str  
#########################################################################


## greedy and non-greedy

st='[Cc]i*.o' # re will match the pattern till the last word of the line
st='[Cc]i*.+?o' # re will match the pattern till the first word
st='Ci*\s.+?o'  # re \s will match the space char   
st='Ci*\S.*?o'  # re \S will match the non-space char (ci2co,cico,cio)

###############################################################################

import re

with open('comparison_file.txt','r') as testfile:
    check_file=testfile.read()

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



