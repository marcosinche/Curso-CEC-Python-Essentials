# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:31:02 2021

@author: marco.sinche
"""

frase_larga=input("Ingrese una frase: ")
letra=input("Letra a contar en la frase: ")
conteo=0
for control in frase_larga:
    if control == letra:
        conteo+=1
print(conteo)


frase_long=input("Ingrese una frase: ")
ltr=input("Letra a contar en la frase: ")
cont=0
var=0
while var<len(frase_long):
    if frase_long[var] == ltr:
        cont+=1
    var+=1
print(cont)