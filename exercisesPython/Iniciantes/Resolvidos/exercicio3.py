# coding: utf-8
#3) Leia um caractere e informe se ele é vogal ou consoante.

#Se prestar bastante atenção, vai perceber que a solução do exercício 2 é exatamente igual ao do exercício 3
caractere = input("Informe o caractere que deseja verificar: ")
caracteresNumerais = "aeiou"
paraLooping = False
contador = 0

while(not paraLooping and contador < len(caracteresNumerais)):
    if (caractere == caracteresNumerais[contador]):
        paraLooping = True
    contador += 1

if(not paraLooping):
    print("O caractere", caractere, "é um consoante.")
else:
    print("O caractere", caractere, "é uma vogal.")