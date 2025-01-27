

# int_out='''GigabitEthernet0/0     unassigned      YES unset  up                    up      
# GigabitEthernet0/1     unassigned      YES unset  down                  down    
# GigabitEthernet0/2     unassigned      YES unset  down                  down    
# GigabitEthernet0/3     unassigned      YES unset  down                  down    
# GigabitEthernet1/0     unassigned      YES unset  down                  down    
# GigabitEthernet1/1     unassigned      YES unset  down                  down    
# GigabitEthernet1/2     unassigned      YES unset  down                  down    
# GigabitEthernet1/3     unassigned      YES unset  down                  down    
# GigabitEthernet2/0     unassigned      YES unset  down                  down    
# GigabitEthernet2/1     unassigned      YES unset  down                  down    
# GigabitEthernet2/2     unassigned      YES unset  down                  down    
# GigabitEthernet2/3     unassigned      YES unset  down                  down    
# Loopback1              1.1.1.2         YES manual up                    up      
# Vlan1                  192.168.40.20   YES manual up                    up   
# '''


# split_input= int_out.splitlines()
# # int_cmd=split_input.s
# # print(split_input)

# for line in split_input:    
#     # print(line)
#     sys_cmd=line.split()
#     if sys_cmd[1]== 'unassigned':
#         continue
#     print(f'interfaces name {sys_cmd[0]} and the ip are {sys_cmd[1]} \n')


##!######################!!##################!!!###########################################################!!!##
######## accesss file from the system and read it #########################################

with open('output.txt','r') as file:
    out_line=file.readlines()
    # print(out_line)
    print('enter to continue...')
    
    for line in out_line:
        if input()=='':
            split_lines=line.strip('\n')
            res=split_lines
            print(split_lines,end='')

######################################################################################



