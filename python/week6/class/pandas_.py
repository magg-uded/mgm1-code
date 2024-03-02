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
''''
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
'''

#selecting data from pandas DF
import pandas as pd

data = {
    'name': ['alice', 'bob', 'charlie'], 
    'age': [23, 45, 13], 
    'city': ['new york', 'los angeles', 'nairobi']
    }

df = pd.DataFrame(data)

print(df['name']) #select from single column
print(df[['name', 'age']]) #select multiple columns
print(df.loc[0]) #select rows by index
print(df[df['age'] > 30])

#adding a new column a pandas DF
import pandas as pd

data = {
    'name': ['alice', 'bob', 'charlie'], 
    'age': [23, 45, 13], 
    'city': ['new york', 'los angeles', 'nairobi']
    }

df = pd.DataFrame(data)

df['salary'] = [50000, 60000, 70000]
print(df)

#grouping data in a pandas DF
import pandas as pd

data = {
    'name': ['alice', 'bob', 'charlie'], 
    'age': [23, 45, 13], 
    'city': ['new york', 'los angeles', 'nairobi'],
    'salary': [50000, 60000, 70000]
    }

df = pd.DataFrame(data)

grouped = df.groupby('age')['salary'].mean() #group by age and get average salary for each group
print(grouped)

