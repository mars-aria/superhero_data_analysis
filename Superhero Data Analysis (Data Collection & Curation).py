#!/usr/bin/env python
# coding: utf-8

# # Superhero (and Villain) Data Analysis

# Below I analyze some data on the Gender characteristic of Superheroes and Villains to determine the ratio of female characters that appear in comic books compared to their male counterparts.

# **References**
# 
# • Domo Fun Sample DataSets:
#   https://domohelp.domo.com/hc/en-us/articles/360043931814-Fun-Sample-DataSets
#   
# • Kaggle Data Set: https://www.kaggle.com/claudiodavi/superhero-set/home
#   *Contains approximately 734 data points with 11 attributes.
# 
# • Pandas To CSV | pd.DataFrame.to_csv():
#   https://www.youtube.com/watch?v=UE0BbRdEFYA

# In[1]:


import pandas as pd

import numpy as np

df = pd.read_csv('heroes_information.csv')


# I start my data analysis process by seeing where the data begins and where it ends.

# In[2]:


#where the data begins
df.head()


# In[3]:


#where the data ends
df.tail()


# I use the len() function to find out the length of the data set:

# In[4]:


print(len(df))


# I also find out the the data frame type by using the type() function:

# In[5]:


print(type(df))


# # Counting the Data (Total Sum)

# Here I count the total values in the "Gender" column: 

# In[6]:


df['Gender']


# I also perform a test by calling the start index number of the "Gender" column:

# In[7]:


df['Gender'][0]


# # Checking the Data Types

# Here I use the type() function to find out the data type of the "Gender" column:
# 

# In[8]:


print(type(df['Gender']))


# I also print the column types using the type() function:

# In[9]:


for col in df.columns:
    print(col, type(df[col][0]))


# # Quantitative Characteristics (Descriptive Statistical Data)

# Using the describe() function, I take a look at the potential quantitative characteristics present in the data:

# In[10]:


df.describe()


# # Checking for Null Values in the Data

# I check for the presence of any null values in order to increase the accuracy of the results:

# In[11]:


df.isnull().sum()


# # Cleaning the Data (Curation)

# To cleanse the data, I replace all the null values in the "Publisher" and "Weight" columns with the value "none":

# In[12]:


df["Publisher"].fillna("none", inplace = True)
df.isnull().sum()


# In[13]:


df["Weight"].fillna("none", inplace = True)
df.isnull().sum()


# I also remove the "Unnamed" column using the drop() function since it appears to have low relevance to my analysis.

# In[14]:


df.drop(df.columns[[0]], axis = 1, inplace = True)


# Lastly, I check the start and end of the data again to make sure the adjustments have been made correctly. 

# In[15]:


df.head()


# In[16]:


df.tail()


# # Counting the Data (Individual Sums)

# Here I count the separate sums of male and female values in the "Gender" column: 
# 

# In[17]:


df['Gender'].value_counts()


# Then I assign a variable to the total sum of "Gender" values:

# In[18]:


#assigning a variable to the total sum of gender values
gender_counts = df['Gender'].value_counts()


# # Renaming a Value 

# For the sake of clarity, I rename the "-" value as "Other" in the "Gender" column.

# In[19]:


#rename "-" value as "Other" in the Gender col

df['Gender'] = df['Gender'].replace({'-': 'Other',
                                    })


# # Visualizing the Data (Results)

# In[20]:


import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20,10)
gender_counts.plot.bar()
plt.title('Gender Ratio of Superheroes & Villains in Comic Books [June 2017]', fontweight ='bold', fontsize = 20)
plt.xlabel('Gender', fontweight ='bold', fontsize = 15)
plt.ylabel('Number of Observations', fontweight ='bold', fontsize = 15)

#show bars with different colors
bars = ('Male', 'Female', 'Other')
x_pos = np.arange(len(bars))
bar_heights = [505, 200, 29]
plt.bar(x_pos, bar_heights, color=['chartreuse', 'cyan', 'magenta'])

#show bars with matching colors on legend
bar_1 = mpatches.Patch(color='chartreuse', label='Male')
bar_2 = mpatches.Patch(color='cyan', label='Female')
bar_3 = mpatches.Patch(color='magenta', label='Other')
plt.legend(handles=[bar_1,bar_2,bar_3], loc='upper right', title='Legend')

#show value names on the x-axis
plt.xticks(x_pos, bars, rotation=0, fontweight ='bold', fontsize = 10)
plt.show()


# # Analyzing the Results (Conclusion) 

# According to the qualitative data collected in June of 2017, female characters make up less than 1/2 of the Superheroes and Villains in the comic books of this dataset. Although the unequal ratio in this outcome was to be expected, the presence of a third unnamed value within the Gender category was not. I hypothesize that this third bar on the graph is representative of residual null values or possibly of characters with other gender identities. I think the most important aspect that can be taken away from my data analysis is that the inclusion of female characters continues to be just as unfairly lacking in the fictional world of comic books as it is in the real world within many male-dominated areas. However, considering that the data used in this analysis is about 5 years old, it is possible that the number of female Superheroes and Villains could have increased since then.
