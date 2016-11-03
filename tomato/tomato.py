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
import skfuzzy as fuzz


#Input
inp = [0.0,2.0,3.0]
#inp = 2.0

universo = np.arange(0,10,0.001)

#Antecedent membership functions
green = [0.0, 3.0, 4.0]
#yellow = [5.0, 5.5, 6.0]
red = [7.0, 8.0, 10.0]

redY = []
greenY = []
yellowY = []
for i in np.arange(0,10,0.1):
	redY.append(membership.triang(i,red[0],red[1],red[2]))
	greenY.append(membership.triang(i,green[0],green[1],green[2]))
	#yellowY.append(membership.triang(i,yellow[0],yellow[1],yellow[2]))


#Consequent membership functions
unripe = [0.0, 3.0, 4.0]
#halfripe = [4.0, 5.0, 6.0]
ripe = [6.0, 7.0, 10.0]

unripeY = []
#halfripeY = []
ripeY = []
for i in np.arange(0,10,0.1):
	unripeY.append(membership.triang(i,unripe[0],unripe[1],unripe[2]))
	#halfripeY.append(membership.triang(i,halfripe[0],halfripe[1],halfripe[2]))
	ripeY.append(membership.triang(i,ripe[0],ripe[1],ripe[2]))

#Rules
out = []
#Rule 1: If a tomato is red then the tomato is ripe
regra1_subsethood_kosko = subsethood.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2])
regra1 = []
for i in np.arange(0,10,0.001):
	regra1.append(np.fmin(regra1_subsethood_kosko,membership.triang(i,ripe[0],ripe[1],ripe[2])))

#Rule 2: If a tomato is green then the tomato is unripe
regra2_subsethood_kosko = subsethood.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2])
regra2 = []
for i in np.arange(0,10,0.001):
	regra2.append(np.fmin(regra2_subsethood_kosko,membership.triang(i,unripe[0],unripe[1],unripe[2])))


## Agregacao das regras
agregacao = np.fmax(regra1,regra2)

grau0 = np.zeros_like(universo)	#variavel auxiliar para montar o grafico

## Calculo do resultado defuzzificado
grau_def = fuzz.defuzz(universo, agregacao, 'centroid')		#defuzzificacao pelo metodo centroide
grau_ativacao = fuzz.interp_membership(universo, agregacao, grau_def)	#intersecao do risco defuzzificado com a funcao de pertinencia

print "grau de amadurecimento: "+str(grau_def)

#Plot
pl.plot(np.arange(0,10,0.1),unripeY,'g--')
pl.plot(np.arange(0,10,0.1),ripeY, 'r--')
pl.fill_between(universo, grau0, agregacao, facecolor='Orange', alpha=0.7)
pl.plot([grau_def, grau_def], [0, grau_ativacao], 'k', linewidth=1.5, alpha=0.9)
pl.axis([0, 10, 0, 1])

pl.show()
