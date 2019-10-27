#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # Chapter-013-02-Retrieve-Location-01

# In[29]:


import datetime
import os
nowStart = datetime.datetime.now()


# In[30]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/04-Location'))
print(dirname)


# ![RIF Functional Layer - Retrieve Step](../../../../../images/DV-Location.JPG)

# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[31]:


setnr=1
filename='13-02-Retrieve-Location-%06d.csv' % setnr
fileZipname=filename + '.gz'
print(fileZipname)


# In[32]:


import pandas as pd
import zipfile as zp


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[33]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[34]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Create Location

# In[35]:


dirDataName = os.path.abspath('../../../../../Data/Chapter 13/000-ExternalData/04-Location/')
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# ## Get Location

# In[36]:


fileZipName='Location-%06d.zip' % setnr
fileDataName='Location-%06d.csv' % setnr
fileFullZipName= os.path.join(pathRealDataName, fileZipName)
print(fileFullZipName)


# In[37]:


with zp.ZipFile(fileFullZipName) as z:
    with z.open(fileDataName) as f:
        locationDF = pd.read_csv(f, header=0, delimiter=',')


# In[38]:


locationDF.index.name='IDKey'
print(locationDF.shape)
print(locationDF.head())


# In[39]:


locationDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[40]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




