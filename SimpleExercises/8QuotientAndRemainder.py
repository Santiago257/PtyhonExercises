#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

import re


a = int(input("Write the first number "))
b = int(input("Write the second number "))

cociente = a / b
residuo = a % b

print("El cociente es ",round(cociente,2))
print("El residuo es " , residuo)