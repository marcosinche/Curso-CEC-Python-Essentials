# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:00:11 2021

@author: marco.sinche
"""

print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")
#La función print permite mostrar un mensaje en la pantalla; en este caso, una cadena.

print()
#Para insertar una línea en blanco, se pude usar esta función: print()

interacción1=input("Primera Interacción, ingrese un valor cualquiera: ")
#Se está generando una variable al escribir "interacción="
print(type(interacción1))

print()
#Línea en blanco

interacción2=input("Segunda Interacción, ingrese un valor cualquiera: ")
#Se está generando una variable al escribir "interacción="
print(type(interacción2))

print()
#Línea en blanco

interacción3=input("Tercera Interacción, ingrese un valor cualquiera: ")
#Se está generando una variable al escribir "interacción="
print(type(interacción3))

print()
#Línea en blanco

interacción4=input("Cuarta Interacción, ingrese un valor cualquiera: ")
#Se está generando una variable al escribir "interacción="
print(type(interacción4))

print()
#Línea en blanco

interacción5=input("Quinta Interacción, ingrese un valor cualquiera: ")
#Se está generando una variable al escribir "interacción="
print(type(interacción5))
#al colocar int(), se está transformando una cadena en un número.

print()
#Línea en blanco

print("¡YA NO SE HARÁN MÁS INTERACCIONES!")
#Mensaje que indica el final

#Al usar el comando "input()", los valores que vienen a continuación se convierten en cadenas, por ello, como salida siempre aparece "class 'str"