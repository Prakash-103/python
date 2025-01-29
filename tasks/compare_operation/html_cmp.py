import difflib
import webbrowser

with open('sample1.txt','r') as pre_check:
    pre_check_lines = pre_check.readlines() 

with open('sample2.txt','r') as post_check:
    post_check_lines = post_check.readlines()


result_diff=difflib.HtmlDiff().make_file(fromlines=pre_check_lines,tolines=post_check_lines,fromdesc='PRE_CHECK',todesc='POST_CHECK')


#print(result_diff)
webbrowser.open_new_tab(result_diff)


