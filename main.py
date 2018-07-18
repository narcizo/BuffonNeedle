import math, random, sys

def buffon_needle(r=2):
    return random.uniform(0, r) < math.cos(random.uniform(0, math.pi / 2))

def buffon(n=1000000, r=2):
    return sum(map(buffon_needle, [r] * n))

print('Simulacao Agulha de Buffon')
print('Acertos\t Estimativa de PI')

number = 1000000
hits = buffon(number)
print(hits, '\t', float(number / hits))
