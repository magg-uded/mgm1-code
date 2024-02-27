import json

#open json file
with open('data.json', 'r') as file:
    #load json data into a python dictionary
    python_dict = json.load(file) #json.load() function reads json data from file and converts it into python dictionary

#print contents of json data
#print(python_dict)

#create a function to get input and return definition
def get_word_definition (python_dict, key, default_value = None):
    #get word input from user and convert to lower case
    word = input('enter a word: ')

    #check if definition exists, else return None if it does not G
    if word in python_dict:
        return word, python_dict[word]
    else:
        return word, default_value

#call get_word_definition function to get the definition of a word
word_definition = get_word_definition(python_dict, 'Gbanou')
print(word_definition)

