# coding: utf-8
#4) Leia um número e mostre na tela se ele é um número primo ou não.

#De longe este exercício é o mais complicado da lista.
#Utilizamos o operador % modulo que tem como resposta o resto da divisão entre 2 valores

verificarNumero = int(input("Digite o número que deseja verificar: "))

for i in range(2, verificarNumero+1):
	if i != verificarNumero:
		i = verificarNumero % i
		if i == 0:
			print ("O número", verificarNumero, "não é primo")
			break
	else:
		print ("O número", verificarNumero, "é primo")
		break