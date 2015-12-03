import random
import md5
import string
import math

def sorteioVencedor():
	seed = random.SystemRandom()
	vencedor = seed.random()
	return vencedor

def palavraSecreta(tamanho):
	palavra = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(tamanho))
	return palavra

def geradorHash(a,b):
	m = md5.new()
	m.update(str(a) +':'+ b)
	print "Hash gerado do sorteio: " + m.hexdigest()


porcentagemVencedor = sorteioVencedor()
secreta = palavraSecreta(15)
geradorHash(porcentagemVencedor, secreta)


print "--------------------------------"
print "Etapa de compras"
print "--------------------------------"

numeroTickets = None
while not numeroTickets:
    try:
        numeroTickets = int(raw_input("Qual o numero de tickets vendido? "))
    except ValueError:
        print 'Digite um numero inteiro'
print numeroTickets

ticketVencedor = math.ceil((numeroTickets)*(porcentagemVencedor))
print "O ticket vencedor: " + str(ticketVencedor)
print "-----------------"
print "Verificavel: "
print "Porcentagem Vencedor: " + str(porcentagemVencedor)
print "Palavra secreta: " + str(secreta)
print geradorHash(porcentagemVencedor, secreta)

