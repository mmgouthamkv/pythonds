# -*- coding: utf-8 -*-
"""taxcalculation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R2OK8UbKTAuNQE4ujj1zEoeNQh6t2o6e
"""

#calculating tax
income=int(input())
hra=int(input())
otherdeductions=int(input())
remaining_amount=income-hra-otherdeductions
if(remaining_amount<300000):
  print("No Tax")
elif(remaining_amount-300000>300000):
  taxable_amount=remaining_amount-300000
  if(taxable_amount>300000 and taxable_amount<600000):
    print("tax to be paid =",taxable_amount/10)
  else:
    print("tax to be paid=",(taxable_amount*15)//100)

