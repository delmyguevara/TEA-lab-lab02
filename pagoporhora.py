# Tendencias e Innovacion en Tecnologia Agricola (TEA)
#
from unicodedata import numeric


horas = input("horas trabajadas? ")
print(horas)
print(type(horas))
valorPorMinuto = input("valor por minuto? ")
print(valorPorMinuto)
print(type(valorPorMinuto))
numeric = [int(horas) * int(valorPorMinuto)]
print(numeric)