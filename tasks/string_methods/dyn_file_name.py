#  file name will be like: date:time_seq.no_cmd.txt

import datetime





with open('sh_config.txt','r') as file:
    #print (file.read())
    seq=file.readlines()  # read all lines in the file        
    #print(seq) 

now=datetime.datetime.now().replace(microsecond=0)

for cmd in enumerate(seq,start=1):
    file_name=f'{str(now).replace(" ",":")}_{str(cmd[0]).zfill(2)}_{str(cmd[1]).replace(" ","_").strip()}.txt' # converting the exch f-int as str to manupulate it 
    print(file_name)
    
    print(f'{cmd[1]}')
    # with open(file_name,'w') as file1:
    #     file1.write('test write newckewgcw')


