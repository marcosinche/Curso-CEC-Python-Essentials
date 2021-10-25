# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:44:44 2021

@author: marco.sinche
"""

var1="Texto1"
var2=643
var3=4.67
var4="Texto2"

print(f"Variable1:{var1*2}\nVariable2: {var2/var3}\n Variable3: {var3+5}")

var5="Mi nombre es: {},mi apellido es: {}, mi edad es: {}".format("Marco","Sinche",37)
print(var5)

print("Mi nombre es:{2}, mi apellido es: {1}, mi edad es {0}".format("Marco","Sinche",37))

print("Mi nombre es:{nombre}, mi apellido es: {apellido}, mi edad es {edad}".format(nombre="Marco",apellido="Sinche",edad=37))

var_prueba="Mensaje de trabajo para pruebas"
print(var_prueba[0:7])
print(var_prueba[7:])
print(var_prueba[-8:-1])
print(var_prueba[-8:])

var_prueba2="    MENSAJE de TRABAJO para Prebitas    "
print(var_prueba2)

var_2=var_prueba2.upper()

print(var_2)

print(var_prueba2.title())

print(var_prueba2.lstrip())
print(var_prueba2.rstrip())

print(var_prueba2.replace("Prebitas","Pruebitas"))

print(var_prueba2.split())

correo_prueba="markeins314@gmail.com"
print(correo_prueba)
print(correo_prueba.split("@"))
