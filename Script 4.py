# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:09:54 2021

@author: marco.sinche
"""

edad=int(input("Ingrese su edad, en años: "))

if edad<18:
    print("Usted es menor de edad")
elif edad>=18 and edad<45:
    print("Usted es un joven adulto")
elif edad>=45 and edad<60:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")

edad2=int(input("ingrese su edad: "))

if edad2<18:
    print("Usted es menor de edad")
elif edad2<45:
    print("Usted es un joven adulto")
elif edad2<60:
    print("Usted es un adulto")
else:
    print("Usted es un adulto mayor")