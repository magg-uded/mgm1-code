#methods to read a file

#read() - returns entire content of file
file_object = open('2.txt', 'r')
file_contents = file_object.read() #file_content is string that contains entire content of file
file_object.close() #free up resources associated with the file using close() method

print(type(file_contents))

#close() -free up resources associated with the file using close() method

#readline() - read one line of file until it reaches end of that line
#readlines() - returns a list with all lines of the file as individual elements

#methods to create files
#file_object = open('plp_x', 'x') #if you run code again after creation it throws error as file exists
#file_object.close()

#methods to modify files

#append method - if you run code again it duplicates file content
file_object = open('plp_x', 'a')
file_object.write('CGTA\n' 'CAGC\n' 'GOOD MORNING\n')
file_object.close()

#use write() method to delete/ overwrite file content
file_object = open('plp_x', 'a')
file_object.write('CGTA\n' 'GOOD MORNING\n')
file_object.close()

#writelines() method - to write several lines at once
#each string represents a line to be added to the file
#file_object = open('plp_x1', 'x')
#file_object.close()

f = open('plp_x1', 'a')
f.writelines(['\nBABA', '\nMAMA', '\nDADA', '\nKAKA'])
f.close()

#doing multiple operations at once
with open('2.txt', 'r+') as file:
    contents = file.read() #read the contents of the file
    file.write('hello, world')#write to file

#deleting files
import os #module with functions that interact with your operating system

file = 'plp_x1'
if os.path.exists(file): #check if file exists
    os.remove(file) #delete file
    print(f'{file} has been deleted')
else:
    print(f'{file} does not exist')

#context managers
#python constructs that remove need to close file and help access file in particular part of program
with open('2.txt', 'r+') as file: #handles reading, writing and closing
    contents = file.read()
    file.write('hello, world')
