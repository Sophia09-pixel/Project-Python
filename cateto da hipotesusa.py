jeito simples
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adijacente:'))
hi = (co ** 2 + ca ** 2)** (1/2)
print('A hipotenusa vai medir:{:.2f}'.format(hi))

#dois jeitos

import math
co = float(input('Digite o Comprimento do cateto oposto:'))
ca = float(input('Digite o Comprimento do cateto adijacente:'))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir:{:.2f}'.format(hi))
