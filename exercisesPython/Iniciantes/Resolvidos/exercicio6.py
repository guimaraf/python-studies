# coding: utf-8
#6) Crie um algoritmo para fazer o reajuste salarial de um funcionário. Caso ele receba menos que 1.700, calcule um aumento de 10%, caso ele receba mais que 1.700, o ajuste é de 5%.

#Similar a solução do exercício 5, porém neste caso para chegar ao valor da porcentagem, eu estou usando valor de entrada e adicionando a ele a soma de % sem a utilização do caractere especial
#Para melhor entendimento, vou detalhar a solução.

#Iniciando com o valor 1000, então 100% deste valor seria 1000, logo 50% seria 500. Então podemos utilizar a seguinte expressão.
# 1000 - (1000*0.5) = 500
#Na matemática a ordem de resolução é primeiro faça a conta dentro do parênteses. Então teremos a conta
# 1000 - (500) = 500

#No final eu usei o += que é justamente atribuir um valor a variável, que seria igual a variável = variável + novo valor

salarioFuncionario = int(input("Qual é o salário do funcionário? "))

if(salarioFuncionario < 1700):
    salarioFuncionario += salarioFuncionario*0.10
else:
    salarioFuncionario += salarioFuncionario*0.05
print("O funcionário agora recebe, R$",salarioFuncionario,", após o reajuste.")