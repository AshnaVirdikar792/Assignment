# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:20:06 2020

@author: Ashna
"""

#Duplicate values in dataset how to find them and remove them using pandas in python 
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df = pd.read_csv('Data.csv')
 
df =  pd.DataFrame({
       'Country':['France','France','Germany','Italy','Italy'],
    'Age': ['44','44','30','38','38'],
    'Salary': ['72000', '72000', '75000', '61000','61000'],
    'Purchased' : ['No','No','Yes','No','No']
})
 

#Check for duplicate values in rows of dataframe as whole
df.duplicated() 

 #to check the total number of rows that have duplicate values

df.duplicated().sum() 
df.loc[df.duplicated(keep='last')] 

#check just for duplicates in a particular column
df.duplicated(subset=['Salary']) 

#To drop duplicate values -
df.drop_duplicates(keep=False)
