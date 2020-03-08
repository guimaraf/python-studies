# coding: utf-8
#1) Leia três números entrados pelo usuário e mostre na tela qual deles é o maior.

#Solução simples
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if (numero1 >= numero2 and numero1 >= numero3): #Comparação direta dos valores, colocando o operador lógico >= desta forma, mesmo se 2 valores sejam iguais, será apresentado como resultado
    print("O maior número é o", numero1)
elif(numero2 >= numero1 and numero2 >= numero3):
    print("O maior número é o", numero2)
else:
    print("O maior número é o", numero3)