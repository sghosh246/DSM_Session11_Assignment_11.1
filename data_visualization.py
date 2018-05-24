# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:01:02 2018

@author: souravg

"""
"""
This assignment is for visualization using matplotlib:
data to use:
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)
Charts to plot:
1. Create a pie chart presenting the male/female proportion
2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
"""
import pandas as pd
from matplotlib import pyplot as plt
#1.Create a pie chart presenting the male/female proportion
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
df = pd.read_csv(url)
gender_category = ['Male','Female']
no_of_males = len(df[df.sex == 'male'])
no_of_females = len(df[df.sex == 'female'])
proportion_of_male_female = [no_of_males,no_of_females]
colors = ["blue", "red"]
explode = (0.1, 0)  
plt.pie(proportion_of_male_female, labels=gender_category, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Chart presenting the male/female proportion")
plt.show()
#2.Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
plt.scatter(df[df.sex == 'male'].age, df[df.sex == 'male'].fare, label = 'Male', alpha=0.4, color = 'b')
plt.scatter(df[df.sex == 'female'].age, df[df.sex == 'female'].fare, label = 'Female', alpha=0.4, color = 'r')
plt.title('Fare Paid vs Age')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.legend()
plt.show()
