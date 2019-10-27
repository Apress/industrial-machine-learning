#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # Chapter-013-02-Retrieve-Person-01

# In[1]:


import datetime
import os
nowStart = datetime.datetime.now()


# In[2]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/02-Person'))
print(dirname)


# ![RIF Functional Layer - Retrieve Step](../../../../../images/DV-Person.JPG)

# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[3]:


filename='13-02-Retrieve-Person.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[4]:


import pandas as pd


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[5]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[6]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Create Person

# In[8]:


dirDataName = os.path.abspath('../../../../../Data/Chapter 13/000-ExternalData/02-Person/')
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# ## Get First Name

# In[9]:


fileDataName='FirstNamesBoy2018.csv'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[10]:


firstNameDF=pd.read_csv(fileFullDataName, header=0)
firstNameDF.set_index("ID", inplace = True)
firstNameDF.columns=['FirstName']
print(firstNameDF.shape)
print(firstNameDF.head())


# ## Get Last Name

# In[11]:


fileDataName='LastNames150.csv'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[12]:


lastNameRawDF=pd.read_csv(fileFullDataName, header=0)
lastNameRawDF.index.name='IDKey'
lastNameRawDF.shape
lastNameRawDF.head()


# In[13]:


lastName1DF=pd.DataFrame(lastNameRawDF.loc[:, ['ID1','Name1','Cnt1']])
lastName1DF.columns=['ID','LastName','Cnt']
lastName1DF.set_index("ID", inplace = True) 
print(lastName1DF.shape)
print(lastName1DF.head())


# In[14]:


lastName2DF=pd.DataFrame(lastNameRawDF.loc[:, ['ID2','Name2','Cnt2']])
lastName2DF.columns=['ID','LastName','Cnt']
lastName2DF.set_index("ID", inplace = True) 
print(lastName2DF.shape)
print(lastName2DF.head())


# In[15]:


lastName3DF=pd.DataFrame(lastNameRawDF.loc[:, ['ID3','Name3','Cnt3']])
lastName3DF.columns=['ID','LastName','Cnt']
lastName3DF.set_index("ID", inplace = True) 
print(lastName3DF.shape)
print(lastName3DF.head())


# In[16]:


DFs = [lastName1DF, lastName2DF, lastName3DF]
lastNameDF=pd.DataFrame(pd.concat(DFs))
lastNameDF.drop(['Cnt'], axis=1, inplace=True)

print(lastNameDF.shape)
print(lastNameDF.head())


# ## Create First Name with Last Name

# In[17]:


firstNameDF['keyid']=0
lastNameDF['keyid']=0

NameDF=pd.merge(firstNameDF, lastNameDF, how='inner')
NameDF.drop(['keyid'], axis=1, inplace=True)
NameDF.reset_index(inplace=True)
NameDF.index.name='KeyID'
NameDF.columns=['ID','FirstName','LastName']

print(NameDF.shape)
print(NameDF.head())


# In[18]:


NameDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[19]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




