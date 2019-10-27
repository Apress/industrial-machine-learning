#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # Chapter-013-02-Retrieve-Time-02

# In[1]:


import datetime
import os
nowStart = datetime.datetime.now()


# In[3]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/01-Time'))
print(dirname)


# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[4]:


filename='13-02-Retrieve-Time-Time.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[6]:


import pandas as pd


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[7]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[8]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Create Time Satellite

# In[11]:


times = pd.date_range(start='2019/01/01 00:00', end='2019/01/01 23:59', freq='1min')
timesNameDF = pd.DataFrame(times.strftime('%H:%M'))
timesNameDF.index.name='TimeID'
timesNameDF.columns=['Time']


# In[12]:


timesKeyDF = pd.DataFrame(times.strftime('T%H%M'))
timesKeyDF.index.name='TimeID'
timesKeyDF.columns=['TimeKey']


# In[13]:


timesDF=timesKeyDF
timesDF=timesDF.merge(timesNameDF, how='inner', left_on='TimeID', right_on='TimeID')


# In[14]:


timesDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[15]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




