import os
#specify the directory you want to list
dic_path='/'

#list all the files and directories in the specified path
contents=os.listdir(dic_path)

# print each file and directory name
for item in contents:
    print(item)