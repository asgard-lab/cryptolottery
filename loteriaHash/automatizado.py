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

def sorteio():
	porcentagemVencedor = sorteioVencedor()
	secreta = palavraSecreta(15)
	m = md5.new()
	m.update(str(porcentagemVencedor) +':'+ secreta)


	numeroTickets = 10000


	ticketVencedor = math.ceil((numeroTickets)*(porcentagemVencedor))

	return ticketVencedor

resultados = []
for i in range (0,10000):
	resultados.append(sorteio())
media = sum(resultados)/len(resultados)
resultados.sort()
arq = open('./lista.txt', 'w')
arq.writelines(str(resultados))
arq.close
print media