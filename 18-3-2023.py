#!/usr/bin/env python
# coding: utf-8

# In[1]:


#decorator

def dinesh(fnc):
    print("outside dec")
    def inner(a,b):
        print("inside decorator")
        if a<b:
            a,b = b,a
        
        return(fnc(a,b))
    return inner


# In[2]:


@dinesh
def test(a,b):
    print("print inside fnction")
    print(a/b)


# In[3]:


test(2,4)


# In[4]:


#iterator (return) performance tunning

a = [1,2,3,4,5]
b = iter(a)
print(next(b))


# In[5]:


print(next(b))


# In[6]:


def test():
    l  = []
    for i in range(5):
        l.append(i)
    return l
print(test())


# In[15]:


#generator

def test():
    for i in range(5):
        yield i
a = test()


# In[16]:


print(next(a))


# In[17]:


#requestjson

import requests


city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4c4784f2061bb212c329a6c7fbca4069&units=metric'.format(city)

res = requests.get(url)

data = res.json()
print(data)


# In[18]:


#resapiservice

import requests

res = requests.get("https://jsonplaceholder.typicode.com/todos")
data = res.json()
print(data[0].get('userId'))


# In[19]:


#multi threating

#
import time

def test():
    for i in range(5):
        print(i)
        time.sleep(0.5)

start  = time.time()

test()
test()
test()

end = time.time()
print(end-start)


# In[20]:




import threading
import time


def test():
    for i in range(5):
        print(i)
        time.sleep(0.5)

start  = time.time()
t1 = threading.Thread(target = test)
t2 = threading.Thread(target = test)
t3 = threading.Thread(target = test)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()


end = time.time()
print(end-start)


# In[21]:


#list complentation

a = [i for i in range(10) if i%2 == 0]
print(a)


# In[23]:


#dict complentation
a = {i:i**2 for i in range(5)}
print(a)


# In[24]:


#list to dictionary

a = ["hi" , "hello" , "welcome"]
b = [1,2,3]

print(dict(zip(b,a)))


# In[ ]:




