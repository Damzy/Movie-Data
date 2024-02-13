#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


# In[6]:


df = pd.read_csv('Top_Ranked_Real_Movies_Dataset.csv')


# In[ ]:


# Eploratory Data Analysis


# In[7]:


# Display the first few rows of the dataset
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())


# In[ ]:


# Visualization 


# In[8]:


# Plot histogram for movie ratings
plt.figure(figsize=(10, 6))
plt.hist(df['Movie Rating'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Movie Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[9]:


plt.figure(figsize=(8, 8))
ratings_distribution = df['Watch Time'].value_counts()
plt.pie(ratings_distribution, labels=ratings_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Watch Time')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[10]:


import seaborn as sns

# Generating random data for demonstration
np.random.seed(0)
ratings = np.random.randint(1, 11, size=1000)  # Random ratings between 1 and 10

# Creating a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=ratings, inner="quartile", color="lightgreen")
plt.title('Violin Plot of Meatscore of movie')
plt.xlabel('Meatscore of movie')
plt.ylabel('Density')
plt.grid(True)
plt.show()


# In[ ]:




