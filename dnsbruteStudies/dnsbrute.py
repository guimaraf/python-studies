import sys
import dns.resolver

argumentos = sys.argv	# le os argumentos do comando
try:
    dominio = argumentos[1]
    lista = argumentos[2]
except:
    print("Faltam argumentos no comando")
    sys.exit(1)

# abre a wordlist
try:
    arquivo = open(lista)
    linhas = arquivo.read().splitlines()
except:
    print("Arquivo nao encontrao ou invalido")
    sys.exit(1)

# para cada linha da wordlist testa o dns
for linha in linhas:
    subdominio = '{}.{}'.format(linha, dominio) # Jogando o primeiro parametro para dentro do codigo
    try:
        respostas = dns.resolver.query(subdominio, 'a')
        for resultado in respostas:
            print (subdominio, resultado)
    except:
        pass


#python dnsbrute.py www.windowsclub.com.br/app/ introNames.txt > exitFile.txt