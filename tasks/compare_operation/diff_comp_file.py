import difflib

from tabulate import tabulate

with open('sample1.txt','r') as pre_check:
    pre_check_lines = pre_check.read() 

with open('sample2.txt','r') as post_check:
    post_check_lines = post_check.read()


result_diff=difflib.Differ().compare(pre_check_lines.splitlines(),post_check_lines.splitlines())

print()

# print(result_diff)
# list1=[]
# list2=[]
# for line in result_diff:  
#     if line.startswith('-'):      
#         # print(line)
#         list1.append(line)
        
#     elif line.startswith('+'):
#         # print(line)
#         list2.append(line)
#     # else:
#     #     print(line) 
# # print (list1)
# # print(list2)

# combined_data = list(zip(list1, list2) )

# # print(combined_data)

# comparison_file=tabulate(combined_data, headers=["PRE_CHECH", "POST_CHECK"], tablefmt="grid")
# with open('comparison_file.txt','w') as file1:
#     file1.write(comparison_file)
