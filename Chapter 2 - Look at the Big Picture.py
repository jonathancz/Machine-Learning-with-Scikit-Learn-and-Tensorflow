#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Chapter 2: End-to-End Machine Learning Project 

# Look at the Big Picture

"""
In this chapter, you will go through an example project end to end, pretending to be a recently hired data scientists 
in a real estate company.
Here are the main steps you will go through:

1. Look at the big picture
2. Get the data
3. Discover and visualize the data to gain insight
4. Prepare the data for Machine Learning algorithms
5. Select a model and train it
6. Fine-tune your model
7. Present your solution
8. Launch, monitor, and maintain your system
"""

# Working with Real Data
"""
Use real data! Fortunately, there are thousands of open datasets to choose from, ranging across all sorts of domains.

Popular open data repositories include:
- UC Irvine Machine Learning Repository
- Kaggle Datasets
- Amazon's AWS datasets
Meta portals (they list open data repositories):
- dataportals.org
- opendatamonitor.eu
- quandl.com
Other pages listing many popular open data repositories:
- Wikipedia's list of Machine Learning datasets
- Quora.com question
- Datasets subreddit


In this chapter we chose the California Housing Prices datasets from the StatLib repository.
This dataset was based on data from the 1990 California census.
It is not recent, but it has many qualities for learning.
"""


# In[9]:


# Download Data

import os
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


# In[10]:


fetch_housing_data()


# In[11]:


import pandas as pd

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[12]:


housing = load_housing_data()
housing.head()


# In[ ]:




