# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:06:55 2021

@author: marco.sinche
"""

var1=1
while var1<10:
    print(var1)
    var1+=1
print("Fin del programa")

num=int(input("Escriba un número positivo:" ))
while num<0:
    print("Número negativo, ingrese otro número")
    num=int(input("Escriba un número positivo: "))
print("El número cumple con la condición")

texto=input("Escriba una palabra o frase: ")
while texto.lower() != "salir":
    print(texto)
    texto=input("Ingrese una palabra o frase: ")
print("Programa terminado")