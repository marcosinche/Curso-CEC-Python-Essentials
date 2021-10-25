# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:03:28 2021

@author: marco.sinche
"""

control:True
while control==True:
    user=input("Ingrese una palabra o frase: ")
    if user.lower() == "salir":
    break
    print(user)
print("Programa terminado")