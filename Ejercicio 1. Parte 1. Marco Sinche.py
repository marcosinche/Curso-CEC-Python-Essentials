# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:12:08 2021

@author: marco.sinche
"""

print("Empezando a trabajar con Python")
#La función print permite mostrar un mensaje en la pantalla; en este caso, una cadena.

print("Realizado por: 'Marco Sinche'")
#Si se desea que una palabra o frase dentro d euna cadena salga entre comillas, se la debe colocar entre comillas sencillas.

print()
#Para insertar una línea en blanco, se pude usar esta función: print()

print("Consultando los tipos de valores: ")
#Si se desea que una palabra o frase dentro d euna cadena salga entre comillas, se la debe colocar entre comillas sencillas.

print()
#Línea en blanco

print("El tipo de dato de 875 es:")
print(type(875))
#La función type() devuelve el tipo o clase de dato al que corresponde un valor ingresado. Así, "int" significa "entero", "float" es "decimal", "complex" es "complejo" y "str" es una cadena. 

print()
#Línea en blanco

print("El tipo de dato de 4.89 es:")
print(type(4.89))
#Al anidar la función type() dentro de la función print(), se imprime el tipo de dato al que corresponde el valor ingresado.

print()
#Línea en blanco

print("El tipo de dato del texto: Now is better than ever. es:")
print(type("Now is better than ever."))
#Los textos o cadenas se deben colocar entre comillas; lo snúmeros no.

print()
#Línea en blanco

print("El tipo de dato de 1.32 es:")
print(type(1.32))
#Float corresponde a un número decimal.

print()
#Línea en blanco

print("¿El valor 5 + 8i corresponde a un valor entero?")
print(isinstance(5+8j,int))
#La función isinstance() permite verificar si el valor ingresado corresponde a una clase de dato determinada.

print()
#Línea en blanco

print("¿El valor 8.2 corresponde a un valor entero?")
print(isinstance(8.2,int))
#Si el valor ingresado fuera un entero, la respuesta sería "true"; caso contrario, la respuesa es "false".

print()
#Línea en blanco

print("¿El texto: Readability counts. corresponde a un string?")
print(isinstance("El texto: Readability counts. corresponde a un string",str))
#Si el valor ingresado fuera una cadena, la respuesta sería "true"; caso contrario, la respuesa es "false".
