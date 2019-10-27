#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # Chapter-013-02-Retrieve-Time-01

# In[12]:


import datetime
import pandas as pd
import os
nowStart = datetime.datetime.now()


# In[13]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/01-Time'))
print(dirname)


# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[14]:


filename='13-02-Retrieve-Time-Date.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[15]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[16]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Create Dates Satellite

# In[17]:


dates = pd.date_range(start='2017-1-1', end='2020-12-31', freq='D')


# In[18]:


datesNameDF = pd.DataFrame(dates.strftime('%Y-%m-%d'))
datesNameDF.index.name='DateID'
datesNameDF.columns=['Date']


# In[19]:


datesKey=dates.strftime('D%Y%m%d')
datesKeyDF=pd.DataFrame(datesKey)
datesKeyDF.index.name='DateID'
datesKeyDF.columns=['DateKey']


# In[20]:


datesDF=datesKeyDF
datesDF=datesDF.merge(datesNameDF, how='inner', left_on='DateID', right_on='DateID')


# In[21]:


print(fullRealZipName)
datesDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[22]:


nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




