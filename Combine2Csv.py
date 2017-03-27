# PwxCircleSolver
import itertools
import math
from itertools import combinations
import pandas as pd  
import numpy as np 
import datetime
import sklearn as sk 
import pickle

circle1 = open('circle1.pickle', 'rb')
circle1 = pickle.load(circle1)


circle2 = open('circle2.pickle', 'rb')
circle2 = pickle.load(circle2)


a = pd.Series(circle1, name='Circle1')
b = pd.Series(circle2, name='Circle2')

print len(a) , "this is a"
print len(b) , "this is b"



df = pd.DataFrame(a)
df2 = pd.DataFrame(b)

# dfjoin = pd.DataFrame(a+b)
join = pd.concat([df,df2])
#join = pd.DataFrame.merge([df,df2], left_index=True)

print join
# print (df.head())
# print (df.head(3))
# print (df),(df2)

# print df
#combine the dataframes

# print result




# a.drop_duplicates('Circle1')
# # print result
# print len(df)
# print len(df2)
# # print (circle2)
# print df.columns
# print df2.columns

df.to_csv('new.csv', columns =['Circle1'])
df2.to_csv('new2.csv', columns =['Circle2'])




# # dfall = dfall[dfall.duplicated()]
# columns = ['equat']
# values = pd.read_table('circles')
# print values.head()
