import numpy as np
import pylab as pl
import sys
sys.path.insert(0, '../')

import mamdani
import similarity
import sigma_meet
import subsethood
import membership
import math
import scipy.integrate as integrate


#Input
#inp = [3.0,3.0,3.0]
inp = 2.0

#Antecedent membership functions
green = [0.0, 3.0, 4.0]
yellow = [5.0, 5.5, 6.0]
red = [7.0, 8.0, 10.0]

redY = []
greenY = []
yellowY = []
for i in np.arange(0,10,0.1):
	redY.append(membership.triang(i,red[0],red[1],red[2]))
	greenY.append(membership.triang(i,green[0],green[1],green[2]))
	yellowY.append(membership.triang(i,yellow[0],yellow[1],yellow[2]))


#Consequent membership functions
unripe = [0.0, 3.0, 4.0]
halfripe = [4.0, 5.0, 6.0]
ripe = [6.0, 7.0, 10.0]

unripeY = []
halfripeY = []
ripeY = []
for i in np.arange(0,10,0.1):
	unripeY.append(membership.triang(i,unripe[0],unripe[1],unripe[2]))
	halfripeY.append(membership.triang(i,halfripe[0],halfripe[1],halfripe[2]))
	ripeY.append(membership.triang(i,ripe[0],ripe[1],ripe[2]))

#Rules
out = []
#Rule 1: If a tomato is red then the tomato is ripe
if mamdani.ativa_regra_crisp(red[0],red[1],red[2],inp) > 0:
	grau = mamdani.ativa_regra_crisp(red[0],red[1],red[2],inp)
	for i in np.arange(0,10,0.1):
		if mamdani.ativa_regra_crisp(ripe[0],ripe[1],ripe[2],i) < grau:
			out.append(mamdani.ativa_regra_crisp(ripe[0],ripe[1],ripe[2],i))
		else:
			out.append(grau)

#Rule 2: If a tomato is green then the tomato is unripe
if mamdani.ativa_regra_crisp(green[0],green[1],green[2],inp) > 0:
	grau = mamdani.ativa_regra_crisp(green[0],green[1],green[2],inp)
	for i in np.arange(0,10,0.1):
		if mamdani.ativa_regra_crisp(unripe[0],unripe[1],unripe[2],i) < grau:
			out.append(mamdani.ativa_regra_crisp(unripe[0],unripe[1],unripe[2],i))
		else:
			out.append(grau)

#Centroid defuzzification
num = np.multiply(np.arange(0,10,0.1),out)
num = integrate.simps(num)
den = integrate.simps(out)
print "grau de amadurecimento: "+str(num/den)

#Plot
pl.plot(np.arange(0,10,0.1),unripeY,'r--', label='mamdani')
pl.plot(np.arange(0,10,0.1),halfripeY, 'g--', label='similaridade')
pl.plot(np.arange(0,10,0.1),ripeY, 'y--', label='sigma-meet')
pl.plot(np.arange(0,10,0.1),out,'b')
pl.fill(np.arange(0,10,0.1),out,'b')
pl.axis([0, 10, 0, 1])

pl.show()