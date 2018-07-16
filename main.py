import random
import math
import sys

def buffon(n,a,b):
    print 'Simulacao Agulha de Buffon'
    print 'agulha = '+str(a) + '  espaco = '+str(b) + "  numero de agulhas = "+str(n)
    print 'Num Acertos   estimativa de PI    '

    nhits = 0
    for i in range(n):
        xcentro = random.uniform(0, b/2.0)  #centro da agulha
        tau=2
        while tau > 1 :
            dx = random.uniform(0,1)
            dy = random.uniform(0,1)
            tau = math.sqrt(dx**2 + dy**2)
            if tau <= 1:
                xponta  = xcentro - (a/2.0)*dx/tau
                if xponta < 0 :
                    nhits += 1
        if(nhits != 0):
            c = 2.0*a*n
            d = b*nhits
            sys.stdout.write("%d               %f\r" % (nhits, c/d))
    print str(nhits)+'                '+str(c/d)


n=2000000  #iteracoes
a = 1   #agulha
b = 2   #espacamento

hits= buffon(n,a,b)
