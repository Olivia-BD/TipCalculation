#!/usr/bin/env python
# coding: utf-8

# In[6]:


Q1=input("How much is your original bill? ")
Q2=input("What percentage is your tip? ")
Tip=round(float(Q2.strip("%"))/100*float(Q1),2)
TotalBill=round((float(Q1)+Tip),2)
print("Your tip based on "+Q2+" is "+str(Tip))
print("Your total bill is "+str(TotalBill))


# In[ ]:




