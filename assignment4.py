# -*- coding: utf-8 -*-
"""assignment4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aqPKl_zvE3IlNfB7GE8oiM2aeLTT7Idn
"""

n=int(input())
c=0
for i in range(2,int(n**0.5)):
  if(n%i==0):
    c+=1
if(c>0):
  print("not a prime number")
else:
  print("prime number")
if(n%5==0):
  print("divisible by 5") 
else:
  print("not divisible by 5")
if(n%2==0):
  print("even number")
else:
  print("odd number")

