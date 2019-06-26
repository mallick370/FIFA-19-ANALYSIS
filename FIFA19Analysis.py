# -*- coding: utf-8 -*-
"""
Created on Sun May 19 09:52:04 2019

@author: KIIT
"""

import pandas as pd
import numpy as np
import matplotlib

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('FIFA19.csv')
print(df.head())

import matplotlib.pyplot as plt
plt.hist(df['Age'],edgecolor='black')
plt.xlabel('Players Age')
plt.ylabel('Number of players')
plt.show()
oldest = df.loc[df['Age'].idxmax()]
print("The oldest player in FIFA 19 is", df['Age'].max(), "years old. His name is", oldest['Name'], 
      'he is from',oldest['Nationality'],'and plays for',oldest['Club'],'.')
print('The median age of a player on FIFA 19 is', np.mean(df['Age']))
youngest = df.loc[df['Age'].idxmin()]
print('The youngest players is',df['Age'].min(), "years old. His name is", youngest['Name'], 
      'he is from',youngest['Nationality'],'and plays for',youngest['Club'],'.')


#KNOWING THE BEST PLAYER IN FIFA 19
plt.hist(df['Overall'],edgecolor='black')
plt.xlabel('Players Rating')
plt.ylabel('Number of players')
plt.show()
best = df.loc[df['Overall'].idxmax()]
print("The best player in FIFA 19 is", df['Overall'].max(), "overall. His name is", best['Name'], 
      'he is from',best['Nationality'],'and plays for',best['Club'],'.')
print('The median rating of a player on FIFA 19 is', np.mean(df['Overall']))
worst = df.loc[df['Overall'].idxmin()]
print('The worst players is',df['Overall'].min(), "overall. His name is", worst['Name'], 
      'he is from',worst['Nationality'],'and plays for',worst['Club'],'.')


df1 = df.query("Overall>=88")
print(df1.head())
#Getting rid of all the elements that makes difficult to convert the different columns datatypes
df1['Value'] = df1['Value'].str.replace('€', '')
#df1['Value'] = df1['Value'].str.replace('K', '000')
df1['Value'] = df1['Value'].str.replace('M', '')
df1['Wage'] = df1['Wage'].str.replace('€', '')
df1['Wage'] = df1['Wage'].str.replace('K', '')

# Changing the datatypes of the selected columns
df1.Value = df1.Value.astype('float')
df1.Wage = df1.Wage.astype('int')
df1.Name = df1.Name.astype('category')

import seaborn as sns
plt.figure(figsize=(10, 10))
df2 = df1.sort_values(['Value'])
sns.barplot(x = "Name" , y  = 'Value', data = df2 ,order = df2['Name'], 
             palette = 'rocket')
plt.title("Value of players (In millions)")
plt.xticks(rotation = 90)


plt.figure(figsize=(10, 10))
df2 = df1.sort_values(['Wage'])
sns.barplot(x = "Name" , y  = 'Wage', data = df2 ,order = df2['Name'], 
             palette = 'rocket')
plt.title("Wage Of players (In K)")
plt.xticks(rotation = 90)