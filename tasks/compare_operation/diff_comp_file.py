import difflib

with open('sample1.txt','r') as pre_check:
    pre_check_lines = pre_check.readlines() 

with open('sample2.txt','r') as post_check:
    post_check_lines = post_check.readlines()


result_diff=difflib.Differ().compare(pre_check_lines,post_check_lines)


print(result_diff)

for line in result_diff:  
    # print(line) 
    if line.startswith('+'):      
        print(line)
    elif line.startswith('-'):
        print(line)

