# coding: utf-8
#5) Crie um algoritmo que pergunte ao usuário seu nome e sua idade. Em seguida verifique se a idade é maior ou menor de 18

#Solução bem simples, auto explicativa
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

if(idade < 18):
    print(nome, 'você é menor de idade e tem,',idade)
else:
    print(nome, 'é maior de idade e tem,',idade)