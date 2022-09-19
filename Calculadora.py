# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:11:02 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def calculadora(num1, num2, operador):
    if (operador == "+"):
        proceso = num1 + num2
    elif (operador == "-"):
        proceso = num1 - num2
    elif (operador == "*"):
        proceso = num1 * num2
    elif (operador == "/"):
        proceso = num1 // num2
    elif (operador == "%"):
        proceso = num1 % num2
    else:
        return "El operador ingresado no es correcto."
    return proceso


num1 = float(input("Ingrese un valor: "))
operador = input("Ingrese un operador (+, -, *, /, %): ")
num2 = float(input("Ingrese un segundo valor: "))

resultado = calculadora(num1, num2, operador)

# print(resultado)
print(f"El resultado de '{num1} {operador} {num2}' es: {resultado}")
