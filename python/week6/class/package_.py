#package is a way to organize related modules into a single directory hierarchy
#packag simply is a directory containing a special file __init__.py that can be empty or contains python code to initialize the package

'''
creating packages
- create new directory
- add empty __init__.py file
- create one or more python modules in the directory
'''
import mypackage.module1
import mypackage.module2

mypackage.module1.hello()
mypackage.module2.welcome()

