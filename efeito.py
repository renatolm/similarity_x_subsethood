from __future__ import division
import numpy as np
import pylab as pl
import membership
import math

#Input
inp = [5.0,5.5,6.0]

inpY = []
for i in np.arange(0,10,0.001):
	inpY.append(membership.triang(i,inp[0],inp[1],inp[2]))

universo = np.arange(0,10,0.001)

efeito = []
for i in np.arange(0, 10, 0.001):
	entrada = membership.triang(i, inp[0], inp[1], inp[2])
	efeito = efeito + (1 - math.cos(math.pi*((entrada)**0.25)))

#Plot
pl.plot(universo,efeito, 'r--')
pl.plot(universo,inpY, 'b')
#pl.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
#pl.fill_between(universo, grau0, agregacao, facecolor='Orange', alpha=0.7)
#pl.plot([grau_def, grau_def], [0, grau_ativacao], 'k', linewidth=1.5, alpha=0.9)
pl.axis([0, 10, 0, 1])
