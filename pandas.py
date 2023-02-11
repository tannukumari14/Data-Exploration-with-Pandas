##### convert all the header to lower case

import pandas as pd
from matplotlib import pyplot as plt 
file=pd.read_csv(r"C:\Users\tanu.b.kumari\Desktop\Assignment-3_Students_performance\Assignment-3_Students_performance\Students_Performance.csv")
file.columns=file.columns.str.lower() 
print(file.head())

### Replace space in headers with underscore( eg. parent eductaion --> parent_education)

file.columns=file.columns.str.replace(" ","_")
print(file.head(10))

### Create new column at the end adding 3 score columns. Header name of column should be total_score

file["total_score"]= file["reading_score"]+file["math_score"]+file["writing_score"]
print(file.head(10))

#### In ethnicity column remove group

file['ethnicity'] = file['ethnicity'].apply(lambda b: str(b).split(' ')[1])
print(file.head(25))

## In test_preparation_course replace none with not_completed

file["test_prepartion_course"]=file["test_preparation_course"].str.replace("none","not_completed ")
print(file.head(25))

### calculate the mean, min and max. score in math_score, reading_score and writing_score and total_score

file.describe(include='all')

### Show statistics for categorical columns like count of each category, mode etc

count = file['ethnicity'].value_counts()
print(count) 

count = file['gender'].value_counts()
print(count) 

### Which gender has better performance in math_score, reading_score, writing_score. ( show Bar plots)

import seaborn as sns
var=["reading_score","total_score","writing_score","math_score"]
fig, ax = plt.subplots(2, 2,figsize =(8, 11))
for var,subplot in zip(var,ax.flatten()):
    a=file.sort_values(by='gender', ascending=True)
    sns.barplot(ax=subplot,data=a,x="gender",y=var)
fig.tight_layout()

# Which Ethnicity has better performance in math_score, reading_score, writing_score. ( Show in bar plots)

import seaborn as sns 
var=["reading_score","total_score","writing_score","math_score"]
fig, ax = plt.subplots(2, 2,figsize =(8, 11)) 
for var,subplot in zip(var,ax.flatten()): 
    a=file.sort_values(by='ethnicity', ascending=False)
    sns.barplot(ax=subplot,data=a,x="ethnicity",y=var) 
    fig.tight_layout()


### Which test_preparation_course category has better performance in math_score, reading_score, writing_score. ( Show in box plots)

var=["reading_score","writing_score","total_score","math_score"]
fig,ax=plt.subplots (2,2,figsize=(14,8))
for var,subplot in zip(var,ax.flatten()):
    sns.boxplot(y=var,data=file,x="test_prepartion_course",ax=subplot)
fig.tight_layout()

### Which lunch category has better performance in math_score, reading_score, writing_score. ( Show in box plots)

var=["reading_score","writing_score","total_score","math_score"]
fig,ax=plt.subplots (2,2,figsize=(14,8))
for var,subplot in zip(var,ax.flatten()):
    sns.boxplot(y=var,data=file,x="lunch",ax=subplot)
fig.tight_layout()

## Create histogram and box plots for math_score, reading_score and writing_score

import seaborn as sns
var=["reading_score","writing_score","total_score","math_score"]
fig,ax=plt.subplots (2,2,figsize=(14,8))
for var,subplot in zip(var,ax.flatten()):
    sns.boxplot(x=var,data=file,ax=subplot)
fig.tight_layout()

file.hist(['math_score',"reading_score","writing_score"])