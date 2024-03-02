#populate empty list using user input via list comprehension 
my_list = [input('enter five words: ') for _ in range(5)]

print('original list: ', my_list)

#populate odd size list using list comprehension
odd_list = [word for word in my_list if len(word) % 2 != 0]

print('new list with odd size: ', odd_list)


    
    
    
    
    
    
    
    