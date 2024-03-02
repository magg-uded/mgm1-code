'''
- pandas is a data manipulation and analysis library for working with structured data
- built on top of numpy
- provides 2 main data structures - series (1-D) and dataframe (2-D)
- offers functions for reading and writing data to and from csv, excel, sql, databases etc
'''

#creating panda dataframe
import pandas as pd

data = {
    'name': ['alice', 'bob', 'charlie'], 
    'age': [23, 45, 13], 
    'city': ['new york', 'los angeles', 'nairobi']
    }

df = pd.DataFrame(data)
print(df)

#reading data from a csv file into pandas DF
