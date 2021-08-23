#Quantos litros de tinta será necessário para pintar essa parede?
largura = float(input('Digite a largura da  parde'))
altura = float(input('Digite a altura da parede'))
area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua area é de {}m2.'.format(largura,altura,area))
tinta = area/2
print('Para pintar essa parede vc irá precisar de {}L de tinta'.format(tinta))
