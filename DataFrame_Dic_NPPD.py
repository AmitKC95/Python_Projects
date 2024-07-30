
import pandas as pd
import numpy as np

states = ['California', 'Texas', 'Florida', 'New York']
population = [354, 342, 543, 3251]

dic_states = {'States':states, 'Population': population}
df_population = pd.DataFrame(dic_states)

print(df_population)




df_exams = pd.read_csv('StudentsPerformance.csv')
print(df_exams.head()) # print(df_exams) for full?


'''
import pandas as pd


df_exams = pd.read_csv('StudentsPerformance.csv')
print(df_exams.head(10)) #for 1st 5, for last 5, try tail
# print(df_exams)

'''print(df_exams.shape) # to list csv table size

pd.set_option('display.max_rows', 25)
print(df_exams)

print(df_exams.index) # max, min can be used with index
max(df_exams.index)

print(df_exams.columns)

print(df_exams.dtypes)

df_exams.info()
print(df_exams.describe())'''

print(df_exams['gender'])

print(df_exams['gender'].index)
print(df_exams['gender'].head())

# print(df_exams.['math_score'])

print(df_exams [['gender', 'math score']])

df_exams['language score'] = 70 #sets all 1k colums with 70value
print(df_exams)

import numpy as np
language_score = np.arange(0,1000)
df_exams ['language score'] = language_score
#sets all 1k colums with value 1 to value 2 and so on
print(df_exams)

int_language_score = np.random.randint(1,100, size = 1000)
df_exams ['language score'] = int_language_score
print(df_exams)

np.random.uniform(1,100, size=100)
print(df_exams)

print(df_exams['language score'].sum()) #count, mean, std, max, min

print(df_exams['gender'].value_counts()) #normalize = true
print(df_exams['parental level of education'].value_counts(normalize=True).round(2))
print(df_exams.sort_values(['math score', 'reading score'], ascending=False, inplace=True))

'''