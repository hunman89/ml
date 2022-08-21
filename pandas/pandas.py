# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd

titanic_df = pd.read_csv('titanic_trains.csv')
print(type(titanic_df))
titanic_df

titanic_df.head(3)

# +

print(titanic_df.shape)
# -

titanic_df.info()

titanic_df.describe()

print(titanic_df['Pclass'].value_counts())

print(titanic_df['Embarked'].value_counts())
print(titanic_df['Embarked'].value_counts(dropna=False))

# +
import numpy as np

col_name = ['col1']
list1 = [1,2,3]
array1 = np.array(list1)

df_list = pd.DataFrame(list1,columns=col_name)
df_array = pd.DataFrame(array1,columns=col_name)
print(df_list)
print(df_array)

# +
col_name = ['col1','col2','col3']
list1 = [[1,2,3],[4,5,6]]
array1 = np.array(list1)

df_list = pd.DataFrame(list1,columns=col_name)
df_array = pd.DataFrame(array1,columns=col_name)
print(df_list)
print(df_array)
# -

dict = {'col1' : [1,2], 'col2' : [2,3]}
print (pd.DataFrame(dict))



print (pd.DataFrame(dict).values)

df = pd.DataFrame(dict)
print (df.values.tolist())
print (df.to_dict('list'))

titanic_df['Age_0'] = 0
titanic_df.head(3)

titanic_df['Age_0'] = titanic_df['Age_0'] + 100
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
titanic_df.head(3)

titanic_df.drop(['Age_0', 'Family_No'], axis=1, inplace=True)
titanic_df.head(3)

indexes = titanic_df.index
print(indexes)
print(indexes.values)

print(indexes[6])

value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
new = value_counts.reset_index(inplace=False)
print(new)

print(titanic_df[['Survived', 'Pclass']].head(3))

titanic_df[0:3]

titanic_df[titanic_df['Pclass'] == 3].head(3)

titanic_df.iloc[:,-1]

titanic_df.iloc[[0,3],4]

titanic_df.loc[3:10, 'Sex':'Ticket']

titanic_df[titanic_df['Age'] > 60][['Name', 'Age']]

con1 = titanic_df['Age'] > 60
con2 = titanic_df['Pclass'] ==1
con3 = titanic_df['Sex'] == 'female'
titanic_df[con1 & con2 & con3]

titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
titanic_sorted.head(3)

titanic_df[['Age', 'Fare']].mean()

titanic_df.head(3)

titanic_df.groupby('Pclass').count()

agg_format = {'Age' : 'max', 'SibSp':'sum', 'Fare': 'mean'}
titanic_df.groupby('Pclass').agg(agg_format)

titanic_df.isna().sum()

titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
titanic_df[['Age', 'Child_Adult']].head(8)


# +
def get_category(age):
    cat=''
    if age <= 5: cat='Baby'
    elif age <= 12: cat= 'Child'
    elif age <= 18: cat= 'Teenager'
    elif age <= 24: cat= 'Student'
    elif age <= 35: cat= 'Young'
    elif age <= 60: cat= 'Adult'
    else : cat = 'Elderly'
        
    return cat

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x: get_category(x))
titanic_df['Age_cat'].value_counts()
