import matplotlib as mpl
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

print('imported')

df_initial=pd.read_csv(r'C:/Users/Jayant/Desktop/DATA-SCIENCE_JOURNEY/titanic/train.csv')

#print(df_initial.columns)
df_initial.describe(include='all')

df=df_initial[['PassengerId', 'Survived', 'Age','Pclass', 'Sex','SibSp',
       'Parch', 'Ticket', 'Fare', 'Embarked']]


sns.swarmplot(x=df.Sex,y=df.Age,hue=df.Survived)

# sex,pclass,sibsp,Embarked