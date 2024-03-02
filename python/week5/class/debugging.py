#using print statement
def add(a, b):
    result = a + b
    print(f'result is {result}')
    return result

result = add(2, 3)
print(f'final result is {result}')

#using pdb
#import pdb; pdb.set_trace() #when this line is executed python stops and waits for you to tell it what to do next

#can also use breakpoint() method to enter debugger easily
#breakpoint()

#using p filename
filename = __file__

import pdb; pdb.set_trace()

print(f'path = {filename}')
