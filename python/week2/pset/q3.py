#a) using inelegant way

bio_data = {} #create empty dictionary to fill with keys and values

for i in range(4):
    #ask user for input
    name = input('enter your name: ')
    nationality = input('enter your country of birth: ')
    fav_color = input('enter your favorite color: ')
    
    #check that user only enters integer value for age
    while True:
        try:
            age = int(input('enter your age: '))
            break
        except ValueError:
            print('please enter integer values only')
    
    #assign values to each key created
    bio_data['name'] = name
    bio_data['age'] = age
    bio_data['nationality'] = nationality
    bio_data['fav_color'] = fav_color
    
    #print dictionary
    print(bio_data)
    
    exit()

#b using dictionary comprehension

bio_data = {key: input(f'enter {key}: ') for key in ['name', 'age', 'height', 'nationality','favorite color']}

print('your biodata: ', bio_data)