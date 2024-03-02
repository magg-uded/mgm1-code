#create file
with open ('my_file.txt', 'x') as file:
    #write to file
    file.writelines(['GTCA', '\n12345', '\nhello, world!'])

#read file content
with open ('my_file.txt', 'r') as file:
    content = file.read()

#print file content
print(content)
