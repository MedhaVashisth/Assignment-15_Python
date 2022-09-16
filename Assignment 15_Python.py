#!/usr/bin/env python
# coding: utf-8

# In[1]:


60*60


# In[2]:


seconds_per_hour = 3600


# In[3]:


seconds_per_day = seconds_per_hour * 24


# In[4]:


seconds_per_day


# In[5]:


seconds_per_day / seconds_per_hour


# In[7]:


seconds_per_day // seconds_per_hour


# In[10]:


def genPrimes():
    primes = [2]
    while True:
        next = primes[-1]
        yield next
        nextPrime = primes[-1] + 1
        count = 0
        answer = False
        while not answer:
            for item in primes:
                if nextPrime % item != 0:
                    count += 1
            if count == len(primes):
                primes.append(nextPrime)
                answer = True
            else:
                nextPrime += 1
                count = 0


# In[ ]:




