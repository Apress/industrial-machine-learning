#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # Chapter-013-02-Retrieve-Time-03

# In[1]:


import datetime
import os
nowStart = datetime.datetime.now()


# In[2]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/01-Time'))
print(dirname)


# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[3]:


filename='13-02-Retrieve-Time.csv'
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


# # Create Date and Time Hub

# In[7]:


dates = pd.date_range(start='2017-1-1', end='2020-12-31', freq='D')


# In[8]:


datesKey=dates.strftime('D%Y%m%d')
datesKeyDF=pd.DataFrame(datesKey)
datesKeyDF.index.name='DateID'

datesKeyDF.columns=['DateKey']
datesKeyDF['Key1']='1'


# In[9]:


times = pd.date_range(start='2019/01/01 00:00', end='2019/01/01 23:59', freq='1min')


# In[10]:


timesKeyDF = pd.DataFrame(times.strftime('T%H%M'))
timesKeyDF.index.name='TimeID'
timesKeyDF.columns=['TimeKey']
timesKeyDF['Key1']='1'


# In[11]:


datetimesDF=datesKeyDF


# In[12]:


datetimesDF=datetimesDF.merge(timesKeyDF, how='inner', left_on='Key1', right_on='Key1')


# In[13]:


datetimesDF.drop('Key1', axis=1, inplace=True)


# In[14]:


datetimesDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[15]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




