# -*- coding: utf-8 -*-
"""database.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pTpmblXPggXpn5eRqHYxAsKNP57qU2rM
"""

roll={} 
for  j in range(2):
  lis=[]
  for i in range(7):
    lis.append(input())
  roll[lis[0]]=lis[1:]  

n=input("Enter roll no.")
print(roll[n])





