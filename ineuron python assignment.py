#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.

# In[35]:


div_7=[]
k=list(range(2000,3201))
final_list=[]

for i in k :
    j = i%7
    if j==0:
        div_7.append(i)
        
for i in div_7 :
    j = i%5
    if j!=0:
        final_list.append(i)
        

final_list


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[121]:


first_name=input('Enter first name: ')
last_name=input("Enter last name: ")


# In[122]:


first_name[::-1] +' '+last_name[::-1]


# 3) Write a Python program to find the volume of a sphere with diameter 12 cm.
#    Formula: V=4/3 * π * r 3
# 

# In[125]:


diameter = 12
r = diameter/2
pi = 22/7


# In[126]:


volume_of_sphere=4/3*pi*r**3


# In[127]:


volume_of_sphere


# In[ ]:





# In[ ]:




