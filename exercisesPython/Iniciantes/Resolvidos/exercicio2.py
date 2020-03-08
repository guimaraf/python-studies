# coding: utf-8
#2) Leia um caractere e informe na tela se ele é um número ou letra.

caractere = input("Informe o caractere que deseja verificar: ")
caracteresNumerais = "0123456789" #Primeiro reservei os caracteres que tem a menor quantidade na comparação, são os números
paraLooping = False #Criei tamém uma variável do tipo booleana para parar o while
contador = 0 #O contador foi criado também para o while, resolvi fazer assim por ser mais simples de entender.

while(not paraLooping and contador < len(caracteresNumerais)): #No while eu fiz uma verificação dupla, primeiro verificar se a variável booleana está falsa.
                                                               #Em seguinda eu verifico se o contador é menor que a quantidade de caracteres da variável caracteresNumerais
    for i in range(0,len(caractere)):
        if (caractere[i] == caracteresNumerais[contador]): #Parando o looping
            paraLooping = True
    contador += 1 #incrementando cado não encontre o caractere

if(not paraLooping): #Por fim, verifico se a variável booleana está falsa, então a resposta é letra
    print("O caractere", caractere, "é uma letra.")
else: #Caso contrário, será um número, pois o bloco do if dentro do while foi executado
    print("O caractere", caractere, "é um número.")