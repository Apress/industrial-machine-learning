#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # 13-02-Assess-03-Object-01

# In[41]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Assess Step](../../../../../images/DV-Object.JPG)

# ![RIF Functional Layer - Assess Step](../../../../../images/RIF-FL-ASS.JPG)

# In[42]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/200-Structured-Zone/'))
print(dirname)


# In[43]:


filename='13-02-Assess-Object.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[44]:


import pandas as pd
import os


# # Load Object

# In[45]:


dirDataName = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/03-Object'))
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[46]:


fileDataName='13-02-Retrieve-Object-000001.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[47]:


objectFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(objectFullDF.shape)


# # Perform Data Quality Checks

# In[48]:


A=objectFullDF
print('A',A.shape)

E=A.drop_duplicates(keep='last')
print('A',E.shape)


# # Create Clean Data

# In[49]:


objectFinalDF=E


# # Create 200-Structured-Zone

# ![Structured Zone](../../../../../images/DL-SZ.JPG)

# In[50]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[51]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Object

# In[52]:


objectFinalDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[53]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




