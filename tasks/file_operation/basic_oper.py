import os


print(os.listdir())

os.chdir(path='/home/root1/Python_for_networking/python/tasks/file_operation')   #manually changing the path environment
print(os.listdir())  # prints the list of files and directories in the current working directory

print(os.getcwd())  # get the curently working directory

print(os.system("ls -l")) # prints the command line inputs

files=os.listdir() # list of files and directories in the current working directory         

for file in files:
    print(file)
    os.system("ls -l "+file ) # prints the details of the file
    print("\n\n\n\n\n\n")
    with open(file, 'r') as f:              # open the file in read mode
        content = f.read()                  
        print(content)


################################################################################################################


file1=open("error_hand.log",'r') # file1 saves the file and the mode to access the file

print(file1.read())     # it prints the output we read 

print(file1.readline()) # it prints the first line of the file
sh_lines=file1.readlines() # it prints the list of lines in the file

for line in sh_lines:
    print(line.rstrip("\n"))    # it removes the \n during the output execution
file1.close()
#################################################################################################################


################## with open ##################################

with open('error_hand.log') as file1:
    command=file1.readlines()  # to describe the output as the array of lines

for cmd in command:
    print(cmd)  #it prints with the \n spaces
    print(cmd.rstrip("\n"))  # it removes the \n during the output execution       

#it auto file close function so we noo need to use file1.close()   

###########################################################################################################

####################### write to file #############################     

with open("error_hand.log",'a') as file2:                      # to apend or write the file
    wr_file=file2.write(" \n added text, \n test to be check!!!")

################################################################################################

##########   copy the data #########

with open('error_hand.log','r') as source:  # it reads the file from the source
    s= source.read()

with open('sample.log','w') as destination: #  it writes the file for duplication
    destination.write(s)

    ####################################################################################################

os.remove('sample.log')  # remove the file permanently
