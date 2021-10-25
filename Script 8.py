# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:07:17 2021

@author: marco.sinche
"""

x=1
while x<=10:
    if x==5:
        x+=1
        continue
    print(x)
    x+=1
    
for i in [78,32,-3,3,56]:
    print("Número")
    print(i)
    
for ch in "PRUEBA":
    print("Repetición")
    print(ch)
    
lst=range(4)
print(lst)

for cut in range(1,6):
    print("Repetición")
    print(cut)

