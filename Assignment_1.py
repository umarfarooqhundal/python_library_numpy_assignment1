#!/usr/bin/env python
# coding: utf-8

# #ASSIGNMENT1 

# In[6]:


import numpy as np


# In[23]:


#Q1
a=np.zeros(10, dtype=int)
print(a)


# In[13]:


#2

b = np.arange(10, 50)
print(b)


# In[24]:


#3
c=np.ones((2,2), dtype=int)
print(c)


# In[25]:


#4
c=np.ones((3,2))
print(c)


# In[32]:


#5 Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones. Use of like functions 

X =np.array([[1,2,3],[9,2,3]])
Y= np.ones_like(X)
print(X)
print(Y)


# In[36]:


#6 Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.

X= np.array([[1,2],[3,4]])
Y= np.zeros_like(X)
print(X)
print(Y)


# In[44]:


# 7 Create a numpy matrix of 4*4 integers, filled with fives.

a= 5* np.ones((4,4), dtype=int)
print(a)


# In[49]:


# 8 Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.

x= np.zeros((2,3), dtype=int)
y= 7*np.ones_like(x)
print(x)
print(y)


# In[74]:


# 9 Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.

I= np.eye(3,3)    
print(I)


# In[66]:


#10 Create a numpy array, filled with 3 random integer values between 1 and 10.

c= np.random.randint(1,11, size=3)
print(c)


# In[76]:


#11 Create a 3*3*3 numpy matrix, filled with random float values.

b= np.random.rand(3,3,3)
print(b)


# In[89]:


#13. Create a numpy array with the odd numbers between 1 to 10

c=np.arange(1,11,2)

print(c)


# In[91]:


# 14. Create a numpy array with numbers from 1 to 10, in descending order.

d= np.arange(10,0,-1)
print(d)


# In[101]:


# 15. Create a 3*3 numpy matrix, filled with values ranging from 0 to 8

c=np.random.randint(8 ,size=(3,3))
print(c)


# # Array Indexation

# In[117]:


# 1 Given the X numpy array, show it's first element
X=np.arange(4,15,2)
print(X)
print(X[0])


# In[116]:


#2 Given the X numpy array, show it's last element

X=np.arange(4,15,2)
print(X)
print(X[-1])


# In[121]:


#3 Given the X numpy array, show it's first three elements

X=np.arange(4,15,2)
print(X)
print(X[:3])


# In[136]:


#4 Given the X numpy array, show all middle elements

X=np.arange(4,15,2)
print(X)
print(X[1:-1])


# In[150]:


#5  Given the X numpy array, show the elements in reverse position.

X=np.arange(4,15,2)
print(X)
print(X[::-1])


# In[154]:


#6 Given the X numpy array, show the elements in an odd position.


X=np.arange(4,15,2)
print(X)
print(X[1::2])


# In[160]:


#7 Given the X numpy matrix, show the first row elements.

X =np.array([[1,2,3],[9,2,3]])
print(X)
print(X[0:1,])


# In[167]:


#8 Given the X numpy matrix, show the last row elements.

X =np.array([[1,8,3],[9,2,3],[0,2,3]])
print(X)
print(X[-1,])


# In[177]:


#9 Given the X numpy matrix, show the first element on first row

X =np.array([[1,8,3],[9,2,3],[0,2,3]])
print(X)
d=  X[0][0]
print(d)


# In[179]:


# 10  Given the X numpy matrix, show the last element on last row.

X =np.array([[1,8,3],[9,2,3],[0,2,3]])
print(X)
d=  X[2][2]
print(d)


# In[181]:


# 11. Given the X numpy matrix, show the first two elements on the first two rows.
X =np.array([[1,8,3],[9,2,3],[0,2,3]])
print(X)
c= X[0:2,0:2]
print(c)


# In[186]:


# 12 Given the X numpy matrix, show the last two elements on the last two rows
a =np.array([[1,8,3],[9,2,3],[0,2,3],[3,4,2],[1,2,3]])
print(a)
c= a[3:5,1:3]
print(c)


# In[ ]:


# ARRAY MANUPLATION 


# In[ ]:


#1. Convert the given integer numpy array to float


# In[192]:


a=np.array(([[1,8,3],[9,2,3],[0,2,3]]))
print(a)
c= np.array(([[1,8,3],[9,2,3],[0,2,3]]) , dtype= float)
print(c)


# In[ ]:


#2 Reverse the given numpy array (first element becomes last)


# In[206]:


a=np.array([1,8,0,2])
print(a)
c= a[::-1]
print(c)


# In[207]:


#3 Given the X numpy array, set the fifth element equal to 1

X= np.array([1,2,3,4,5,6,7,8])
X[4]=1
print(X)


# In[208]:


# 4 Given the X numpy matrix, change the last row with all 1
X= np.array([[1,2,3],[5,6,7]])
X[1]=1
print(X)


# In[209]:


# 5 Given the X numpy matrix, add 5 to every element

X= np.array([[2,3,4],[1,2,3]])
X=X+5
print(X)


# In[ ]:


# END 

