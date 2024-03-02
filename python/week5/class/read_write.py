#there are 4 modes used to open files in python
''' 'r' (read only) - only read content of file'''
file = open('2.txt', 'r') #open file for reading

content = file.read() #read contents of file

print(content) #print content of file
print(file.name)
print(file.closed)
print(file.mode)

file.close() #close file

''' 'w' (write only) - only write to a file'''
file = open('2.txt', 'w') #open file for writing

file.write('XYZX\n') #write some text to file. note this overwrites existing content on file. creates a new file if file does not exist
file.write('HABARI\n')

file.close() #close file

''' other modes
rb -open file for reading only in binary format starting from beginning of file
r+ - open file for reading and writing. file pointer placed at beginning of file
wb - same as w but opens in binary mode
w+ - same as w but allows to read from file
wb+ - same as wb but allows to read from file
a - (append only) append to existing file. data added to end of file
ab - same as a but opens in binary. creates new file if file does not exist
a+ - same as a but also open for reading
ab+ - same as ab but open for reading
x (write only, exclusive creation) - write to a file only if the file does not already exist
'''
