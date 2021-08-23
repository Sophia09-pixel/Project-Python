nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Sophia':
    print('Que nome lindo {}'.format(nome))
else:
    print('Seu nome é tõa comum <D')
print('Bom dia,{}'.format(nome))

n1 = float(input('Digite sua primeira nota'))
n2 = float(input('Digite sua segunda nota'))
n3 = float(input('Digite sua terceira nota:'))
n4 = float(input('Digite sua quarta nota:'))
media = (n1 + n2 + n3 + n4)/4
print('Sua nota foi {:.1f}'.format(media))
if media <= 6:
    print('Voce esta com nota vermelha. Estude mais!!')
else:
    print('Voce esta com media azul, Parabens')
    
  
  #adivinhe o número em que o pc está pensando
    from random import randint
pc = randint(0,5) #faz o pc sortear  o numero
print('-=-' *20)
print('Escolhi um número entre 0 e 5 consegue adivinhar??')
print('-=-' *20)
jogador = int(input('Em qual numero eu pensei: '))
if jogador == pc:
    print('Parabens voce acertou')
else:
    print('ERROUUUUUUUU!!')
    
    
#calculador de multa
velocidade = float(input('Qual  velocidade atual do carro??'))
if velocidade >= 80:
    print('Ta querendo morrer maluko??, Vai levar uma multa por ultrapassar 80km/h')
    multa = (velocidade - 80) * 7
    print('Sua multa é de R$ {:.2f}'.format(multa))
print('tenha um bom dia! Dirija com segurança!')


#numeros impares e pares
n = int(input('Digite um numero:'))
resultado = n % 2 #todo numero par vai dar 0 e todo numero impar vai dar 1
if resultado == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))

#calculador de viajem
distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce ira viajar {} km'.format(distancia))
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('Voce ira pagar R${:.2f}'.format(preco))


#ano bissexto

from datetime import date
ano = int(input('Digite um ano para ser analisado: Ou digite 0 para analisar o ano atual: '))
print('PROCESSANDO...')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
