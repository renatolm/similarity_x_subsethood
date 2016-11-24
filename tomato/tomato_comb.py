import numpy as np
import pylab as pl
import sys
sys.path.insert(0, '../')

import subsethood
import subsethood_wilmot
import subsethood_join_param
import subsethood_meet_param
import membership
import math
import skfuzzy as fuzz


#Input
inp = [3.8,4.0,5.0]

alpha = 0.5
beta = 1 - alpha

inpY = []
for i in np.arange(0,10,0.001):
	inpY.append(membership.triang(i,inp[0],inp[1],inp[2]))

universo = np.arange(0,10,0.001)

#Antecedent membership functions
green = [0.0, 3.0, 4.0]
red = [7.0, 8.0, 10.0]

redY = []
greenY = []
for i in np.arange(0,10,0.001):
	redY.append(membership.triang(i,red[0],red[1],red[2]))
	greenY.append(membership.triang(i,green[0],green[1],green[2]))


#Consequent membership functions
unripe = [0.0, 3.0, 4.0]
ripe = [6.0, 7.0, 10.0]

unripeY = []
ripeY = []
for i in np.arange(0,10,0.001):
	unripeY.append(membership.triang(i,unripe[0],unripe[1],unripe[2]))
	ripeY.append(membership.triang(i,ripe[0],ripe[1],ripe[2]))

#Rules
#Rule 1: If a tomato is red then the tomato is ripe
regra1_subsethood_kosko = subsethood.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2])
regra1_subsethood_wilmot = subsethood_wilmot.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2])
regra1_subsethood_koswil = ((alpha*regra1_subsethood_kosko)+(beta*regra1_subsethood_wilmot))

regra1_subsethood_meet_025 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.25)
regra1_subsethood_join_025 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.25)
regra1_subsethood_025 = ((alpha*regra1_subsethood_meet_025)+(beta*regra1_subsethood_join_025))

regra1_subsethood_meet_05 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.5)
regra1_subsethood_join_05 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.5)
regra1_subsethood_05 = ((alpha*regra1_subsethood_meet_05)+(beta*regra1_subsethood_join_05))

regra1_subsethood_meet_1 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1)
regra1_subsethood_join_1 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1)
regra1_subsethood_1 = ((alpha*regra1_subsethood_meet_1)+(beta*regra1_subsethood_join_1))

regra1_subsethood_meet_2 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],2)
regra1_subsethood_join_2 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],2)
regra1_subsethood_2 = ((alpha*regra1_subsethood_meet_2)+(beta*regra1_subsethood_join_2))


print "ativacao regra 1 koswil: "+str(regra1_subsethood_koswil)
print "ativacao regra 1 meet-join 025: "+str(regra1_subsethood_025)
print "ativacao regra 1 meet-join 05: "+str(regra1_subsethood_05)
print "ativacao regra 1 meet-join 1: "+str(regra1_subsethood_1)
print "ativacao regra 1 meet-join 2: "+str(regra1_subsethood_2)

regra1_koswil = []
regra1_025 = []
regra1_05 = []
regra1_1 = []
regra1_2 = []

for i in np.arange(0,10,0.001):
	regra1_koswil.append(np.fmin(regra1_subsethood_koswil,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_025.append(np.fmin(regra1_subsethood_025,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_05.append(np.fmin(regra1_subsethood_05,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_1.append(np.fmin(regra1_subsethood_1,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_2.append(np.fmin(regra1_subsethood_2,membership.triang(i,ripe[0],ripe[1],ripe[2])))

#Rule 2: If a tomato is green then the tomato is unripe
regra2_subsethood_kosko = subsethood.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2])
regra2_subsethood_wilmot = subsethood_wilmot.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2])
regra2_subsethood_koswil = ((alpha*regra2_subsethood_kosko)+(beta*regra2_subsethood_wilmot))

regra2_subsethood_meet_025 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.25)
regra2_subsethood_join_025 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.25)
regra2_subsethood_025 = ((alpha*regra2_subsethood_meet_025)+(beta*regra2_subsethood_join_025))

regra2_subsethood_meet_05 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.5)
regra2_subsethood_join_05 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.5)
regra2_subsethood_05 = ((alpha*regra2_subsethood_meet_05)+(beta*regra2_subsethood_join_05))

regra2_subsethood_meet_1 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1)
regra2_subsethood_join_1 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1)
regra2_subsethood_1 = ((alpha*regra2_subsethood_meet_1)+(beta*regra2_subsethood_join_1))

regra2_subsethood_meet_2 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],2)
regra2_subsethood_join_2 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],2)
regra2_subsethood_2 = ((alpha*regra2_subsethood_meet_2)+(beta*regra2_subsethood_join_2))


print "ativacao regra 2 koswil: "+str(regra2_subsethood_koswil)
print "ativacao regra 2 meet-join 025: "+str(regra2_subsethood_025)
print "ativacao regra 2 meet-join 05: "+str(regra2_subsethood_05)
print "ativacao regra 2 meet-join 1: "+str(regra2_subsethood_1)
print "ativacao regra 2 meet-join 2: "+str(regra2_subsethood_2)

regra2_koswil = []
regra2_025 = []
regra2_05 = []
regra2_1 = []
regra2_2 = []

for i in np.arange(0,10,0.001):
	regra2_koswil.append(np.fmin(regra2_subsethood_koswil,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_025.append(np.fmin(regra2_subsethood_025,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_05.append(np.fmin(regra2_subsethood_05,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_1.append(np.fmin(regra2_subsethood_1,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_2.append(np.fmin(regra2_subsethood_2,membership.triang(i,unripe[0],unripe[1],unripe[2])))


## Agregacao das regras
agregacao_koswil = np.fmax(regra1_koswil,regra2_koswil)
agregacao_025 = np.fmax(regra1_025,regra2_025)
agregacao_05 = np.fmax(regra1_05,regra2_05)
agregacao_1 = np.fmax(regra1_1,regra2_1)
agregacao_2 = np.fmax(regra1_2,regra2_2)

grau0 = np.zeros_like(universo)	#variavel auxiliar para montar o grafico

## Calculo do resultado defuzzificado
try:
	grau_def_koswil = fuzz.defuzz(universo, agregacao_koswil, 'centroid')		#defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_koswil = 0

try:
	grau_def_025 = fuzz.defuzz(universo, agregacao_025, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_025 = 0

try:
	grau_def_05 = fuzz.defuzz(universo, agregacao_05, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_05 = 0

try:
	grau_def_1 = fuzz.defuzz(universo, agregacao_1, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_1 = 0

try:
	grau_def_2 = fuzz.defuzz(universo, agregacao_2, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_2 = 0


grau_ativacao_koswil = fuzz.interp_membership(universo, agregacao_koswil, grau_def_koswil)
grau_ativacao_025 = fuzz.interp_membership(universo, agregacao_025, grau_def_025)
grau_ativacao_05 = fuzz.interp_membership(universo, agregacao_05, grau_def_05)
grau_ativacao_1 = fuzz.interp_membership(universo, agregacao_1, grau_def_1)
grau_ativacao_2 = fuzz.interp_membership(universo, agregacao_2, grau_def_2)


print "grau de amadurecimento koswil: "+str(grau_def_koswil)
print "grau de amadurecimento meet-join 0.25: "+str(grau_def_025)
print "grau de amadurecimento meet-join 0.5: "+str(grau_def_05)
print "grau de amadurecimento meet-join 1: "+str(grau_def_1)
print "grau de amadurecimento meet-join 2: "+str(grau_def_2)

fig, ((ax0), (ax1), (ax2), (ax3), (ax4)) = pl.subplots(5, 1)
#Plot
#pl.plot(universo,greenY,'g--')
#pl.plot(universo,redY, 'r--')
#pl.plot(universo,inpY, 'b')
#pl.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
#pl.fill_between(universo, grau0, agregacao, facecolor='Orange', alpha=0.7)
#pl.plot([grau_def, grau_def], [0, grau_ativacao], 'k', linewidth=1.5, alpha=0.9)
#pl.axis([0, 10, 0, 1])

ax0.plot(universo, unripeY, 'g--')
ax0.plot(universo, ripeY, 'r--')
ax0.fill_between(universo, grau0, agregacao_koswil, facecolor='Orange', alpha=0.7)
ax0.plot([grau_def_koswil,grau_def_koswil], [0, grau_ativacao_koswil], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title("Kosko+Willmott")

ax1.plot(universo, unripeY, 'g--')
ax1.plot(universo, ripeY, 'r--')
ax1.fill_between(universo, grau0, agregacao_025, facecolor='Orange', alpha=0.7)
ax1.plot([grau_def_025,grau_def_025], [0, grau_ativacao_025], 'k', linewidth=1.5, alpha=0.9)
ax1.set_title("Meet+Join p=0.25")

ax2.plot(universo, unripeY, 'g--')
ax2.plot(universo, ripeY, 'r--')
ax2.fill_between(universo, grau0, agregacao_05, facecolor='Orange', alpha=0.7)
ax2.plot([grau_def_05,grau_def_05], [0, grau_ativacao_05], 'k', linewidth=1.5, alpha=0.9)
ax2.set_title("Meet+Join p=0.5")

ax3.plot(universo, unripeY, 'g--')
ax3.plot(universo, ripeY, 'r--')
ax3.fill_between(universo, grau0, agregacao_1, facecolor='Orange', alpha=0.7)
ax3.plot([grau_def_1,grau_def_1], [0, grau_ativacao_1], 'k', linewidth=1.5, alpha=0.9)
ax3.set_title("Meet+Join p=1")

ax4.plot(universo, unripeY, 'g--')
ax4.plot(universo, ripeY, 'r--')
ax4.fill_between(universo, grau0, agregacao_2, facecolor='Orange', alpha=0.7)
ax4.plot([grau_def_2,grau_def_2], [0, grau_ativacao_2], 'k', linewidth=1.5, alpha=0.9)
ax4.set_title("Meet+Join p=2")

pl.tight_layout()
#pl.show()
pl.savefig("resultados/resultados3_comb_05.png")
