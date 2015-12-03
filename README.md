# cryptolottery

## LoteriaHash 
Essa primeria versão de loteria utiliza um hash md5 para garantir que o resultado final não seja diferente do sorteado antes da venda de ticket.<br>
### Funcionamento
+ Dealer cria uma *secret* key aleatória e a *porcentagem do vencedor*
+ É gerado um hash md5 usando a seguinte entrada: `entrada = "secret:porcentagem"`
+ Esse valor da hash é publicado para todos jogadores
+ Depois de encerrado a venda de tickets, é calculando o vencedor utilizando `nroTicketVencedor = math.ceil(nroTicketsVendidos*porcentagem)`
+ O Dealer publica o vencedor, secret e porcentagem utilizada
+ Jogadores podem usar a função hash para verificar se o valor é válido com o publicado inicialmente

###Automatizado
O automatizado.py é apenas para testes. Ele gera um alto número de sorteios e coloca todos os números vencedores em um arquivo. Isso permite verificar estatisticamente se os resultados aleatórios estão bem destribuídos

