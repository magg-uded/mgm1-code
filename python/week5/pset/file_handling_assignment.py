#create file
with open ('my_file.txt', 'x') as file:
    #write to file
    file.writelines(['\nGTCA', '\n12345', '\nhello, world!'])

#read file content
try:
    with open ('my_file.txt', 'r') as file:
        content = file.read()
except (FileNotFoundError, PermissionError):
    print('file not found or permission denied!')

#print file content
print(content)

#append to file
with open ('my_file.txt', 'a') as file:
    file.writelines(['\nQWERTY0001', '\nplp2024 class', '\n"end="'])
