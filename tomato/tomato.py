import numpy as np
import pylab as pl
import sys
sys.path.insert(0, '../')

import mamdani
import similarity
import sigma_meet
import subsethood
import subsethood_wilmot
import subsethood_join_param
import subsethood_meet_param
import membership
import math
import skfuzzy as fuzz


#Input
inp = [5.0,5.5,6.0]

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
regra1_subsethood_meet_025 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.25)
regra1_subsethood_join_025 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.25)
regra1_subsethood_meet_05 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.5)
regra1_subsethood_join_05 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.5)
regra1_subsethood_meet_1 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1)
regra1_subsethood_join_1 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1)
regra1_subsethood_meet_2 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],2)
regra1_subsethood_join_2 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],2)
regra1_subsethood_meet_10 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],10)
regra1_subsethood_join_10 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],10)
regra1_subsethood_meet_100 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],100)
regra1_subsethood_join_100 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],100)
regra1_subsethood_meet_1000 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1000)
regra1_subsethood_join_1000 = subsethood_join_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1000)

print "ativacao regra 1 kos: "+str(regra1_subsethood_kosko)
print "ativacao regra 1 wil: "+str(regra1_subsethood_wilmot)
print "ativacao regra 1 meet 025: "+str(regra1_subsethood_meet_025)
print "ativacao regra 1 join 025: "+str(regra1_subsethood_join_025)
print "ativacao regra 1 meet 05: "+str(regra1_subsethood_meet_05)
print "ativacao regra 1 join 05: "+str(regra1_subsethood_join_05)
print "ativacao regra 1 meet 1: "+str(regra1_subsethood_meet_1)
print "ativacao regra 1 join 1: "+str(regra1_subsethood_join_1)
print "ativacao regra 1 meet 2: "+str(regra1_subsethood_meet_2)
print "ativacao regra 1 join 2: "+str(regra1_subsethood_join_2)
print "ativacao regra 1 meet 10: "+str(regra1_subsethood_meet_10)
print "ativacao regra 1 join 10: "+str(regra1_subsethood_join_10)
print "ativacao regra 1 meet 100: "+str(regra1_subsethood_meet_100)
print "ativacao regra 1 join 100: "+str(regra1_subsethood_join_100)
print "ativacao regra 1 meet 1000: "+str(regra1_subsethood_meet_1000)
print "ativacao regra 1 join 1000: "+str(regra1_subsethood_join_1000)

regra1_kos = []
regra1_wil = []
regra1_meet_025 = []
regra1_join_025 = []
regra1_meet_05 = []
regra1_join_05 = []
regra1_meet_1 = []
regra1_join_1 = []
regra1_meet_2 = []
regra1_join_2 = []
regra1_meet_10 = []
regra1_join_10 = []
regra1_meet_100 = []
regra1_join_100 = []
regra1_meet_1000 = []
regra1_join_1000 = []
for i in np.arange(0,10,0.001):
	regra1_kos.append(np.fmin(regra1_subsethood_kosko,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_wil.append(np.fmin(regra1_subsethood_wilmot,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_025.append(np.fmin(regra1_subsethood_meet_025,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_025.append(np.fmin(regra1_subsethood_join_025,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_05.append(np.fmin(regra1_subsethood_meet_05,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_05.append(np.fmin(regra1_subsethood_join_05,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_1.append(np.fmin(regra1_subsethood_meet_1,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_1.append(np.fmin(regra1_subsethood_join_1,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_2.append(np.fmin(regra1_subsethood_meet_2,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_2.append(np.fmin(regra1_subsethood_join_2,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_10.append(np.fmin(regra1_subsethood_meet_10,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_10.append(np.fmin(regra1_subsethood_join_10,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_100.append(np.fmin(regra1_subsethood_meet_100,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_100.append(np.fmin(regra1_subsethood_join_100,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_1000.append(np.fmin(regra1_subsethood_meet_1000,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_join_1000.append(np.fmin(regra1_subsethood_join_1000,membership.triang(i,ripe[0],ripe[1],ripe[2])))

#Rule 2: If a tomato is green then the tomato is unripe
regra2_subsethood_kosko = subsethood.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2])
regra2_subsethood_wilmot = subsethood_wilmot.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2])
regra2_subsethood_meet_025 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.25)
regra2_subsethood_join_025 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.25)
regra2_subsethood_meet_05 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.5)
regra2_subsethood_join_05 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.5)
regra2_subsethood_meet_1 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1)
regra2_subsethood_join_1 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1)
regra2_subsethood_meet_2 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],2)
regra2_subsethood_join_2 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],2)
regra2_subsethood_meet_10 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],10)
regra2_subsethood_join_10 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],10)
regra2_subsethood_meet_100 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],100)
regra2_subsethood_join_100 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],100)
regra2_subsethood_meet_1000 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1000)
regra2_subsethood_join_1000 = subsethood_join_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1000)

print "ativacao regra 2 kos: "+str(regra2_subsethood_kosko)
print "ativacao regra 2 wil: "+str(regra2_subsethood_wilmot)
print "ativacao regra 2 meet 025: "+str(regra2_subsethood_meet_025)
print "ativacao regra 2 join 025: "+str(regra2_subsethood_join_025)
print "ativacao regra 2 meet 05: "+str(regra2_subsethood_meet_05)
print "ativacao regra 2 join 05: "+str(regra2_subsethood_join_05)
print "ativacao regra 2 meet 1: "+str(regra2_subsethood_meet_1)
print "ativacao regra 2 join 1: "+str(regra2_subsethood_join_1)
print "ativacao regra 2 meet 2: "+str(regra2_subsethood_meet_2)
print "ativacao regra 2 join 2: "+str(regra2_subsethood_join_2)
print "ativacao regra 2 meet 10: "+str(regra2_subsethood_meet_10)
print "ativacao regra 2 join 10: "+str(regra2_subsethood_join_10)
print "ativacao regra 2 meet 100: "+str(regra2_subsethood_meet_100)
print "ativacao regra 2 join 100: "+str(regra2_subsethood_join_100)
print "ativacao regra 2 meet 1000: "+str(regra2_subsethood_meet_1000)
print "ativacao regra 2 join 1000: "+str(regra2_subsethood_join_1000)

regra2_kos = []
regra2_wil = []
regra2_meet_025 = []
regra2_join_025 = []
regra2_meet_05 = []
regra2_join_05 = []
regra2_meet_1 = []
regra2_join_1 = []
regra2_meet_2 = []
regra2_join_2 = []
regra2_meet_10 = []
regra2_join_10 = []
regra2_meet_100 = []
regra2_join_100 = []
regra2_meet_1000 = []
regra2_join_1000 = []

for i in np.arange(0,10,0.001):
	regra2_kos.append(np.fmin(regra2_subsethood_kosko,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_wil.append(np.fmin(regra2_subsethood_wilmot,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_025.append(np.fmin(regra2_subsethood_meet_025,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_025.append(np.fmin(regra2_subsethood_join_025,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_05.append(np.fmin(regra2_subsethood_meet_05,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_05.append(np.fmin(regra2_subsethood_join_05,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_1.append(np.fmin(regra2_subsethood_meet_1,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_1.append(np.fmin(regra2_subsethood_join_1,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_2.append(np.fmin(regra2_subsethood_meet_2,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_2.append(np.fmin(regra2_subsethood_join_2,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_10.append(np.fmin(regra2_subsethood_meet_10,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_10.append(np.fmin(regra2_subsethood_join_10,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_100.append(np.fmin(regra2_subsethood_meet_100,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_100.append(np.fmin(regra2_subsethood_join_100,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_1000.append(np.fmin(regra2_subsethood_meet_1000,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_join_1000.append(np.fmin(regra2_subsethood_join_1000,membership.triang(i,unripe[0],unripe[1],unripe[2])))


## Agregacao das regras
agregacao_kos = np.fmax(regra1_kos,regra2_kos)
agregacao_wil = np.fmax(regra1_wil,regra2_wil)
agregacao_meet_025 = np.fmax(regra1_meet_025,regra2_meet_025)
agregacao_join_025 = np.fmax(regra1_join_025,regra2_join_025)
agregacao_meet_05 = np.fmax(regra1_meet_05,regra2_meet_05)
agregacao_join_05 = np.fmax(regra1_join_05,regra2_join_05)
agregacao_meet_1 = np.fmax(regra1_meet_1,regra2_meet_1)
agregacao_join_1 = np.fmax(regra1_join_1,regra2_join_1)
agregacao_meet_2 = np.fmax(regra1_meet_2,regra2_meet_2)
agregacao_join_2 = np.fmax(regra1_join_2,regra2_join_2)
agregacao_meet_10 = np.fmax(regra1_meet_10,regra2_meet_10)
agregacao_join_10 = np.fmax(regra1_join_10,regra2_join_10)
agregacao_meet_100 = np.fmax(regra1_meet_100,regra2_meet_100)
agregacao_join_100 = np.fmax(regra1_join_100,regra2_join_100)
agregacao_meet_1000 = np.fmax(regra1_meet_1000,regra2_meet_1000)
agregacao_join_1000 = np.fmax(regra1_join_1000,regra2_join_1000)

grau0 = np.zeros_like(universo)	#variavel auxiliar para montar o grafico

## Calculo do resultado defuzzificado
try:
	grau_def_kos = fuzz.defuzz(universo, agregacao_kos, 'centroid')		#defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_kos = 0

try:
	grau_def_wil = fuzz.defuzz(universo, agregacao_wil, 'centroid')		#defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_wil = 0

try:
	grau_def_meet_025 = fuzz.defuzz(universo, agregacao_meet_025, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_025 = 0

try:
	grau_def_join_025 = fuzz.defuzz(universo, agregacao_join_025, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_025 = 0

try:
	grau_def_meet_05 = fuzz.defuzz(universo, agregacao_meet_05, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_05 = 0

try:
	grau_def_join_05 = fuzz.defuzz(universo, agregacao_join_05, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_05 = 0

try:
	grau_def_meet_1 = fuzz.defuzz(universo, agregacao_meet_1, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_1 = 0

try:
	grau_def_join_1 = fuzz.defuzz(universo, agregacao_join_1, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_1 = 0

try:
	grau_def_meet_2 = fuzz.defuzz(universo, agregacao_meet_2, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_2 = 0

try:
	grau_def_join_2 = fuzz.defuzz(universo, agregacao_join_2, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_2 = 0

try:
	grau_def_meet_10 = fuzz.defuzz(universo, agregacao_meet_10, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_10 = 0

try:
	grau_def_join_10 = fuzz.defuzz(universo, agregacao_join_10, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_10 = 0

try:
	grau_def_meet_100 = fuzz.defuzz(universo, agregacao_meet_100, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_100 = 0

try:
	grau_def_join_100 = fuzz.defuzz(universo, agregacao_join_100, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_100 = 0

try:
	grau_def_meet_1000 = fuzz.defuzz(universo, agregacao_meet_1000, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_1000 = 0

try:
	grau_def_join_1000 = fuzz.defuzz(universo, agregacao_join_1000, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_join_1000 = 0

grau_ativacao_kos = fuzz.interp_membership(universo, agregacao_kos, grau_def_kos)
grau_ativacao_wil = fuzz.interp_membership(universo, agregacao_wil, grau_def_wil)
grau_ativacao_meet_025 = fuzz.interp_membership(universo, agregacao_meet_025, grau_def_meet_025)
grau_ativacao_join_025 = fuzz.interp_membership(universo, agregacao_join_025, grau_def_join_025)
grau_ativacao_meet_05 = fuzz.interp_membership(universo, agregacao_meet_05, grau_def_meet_05)
grau_ativacao_join_05 = fuzz.interp_membership(universo, agregacao_join_05, grau_def_join_05)
grau_ativacao_meet_1 = fuzz.interp_membership(universo, agregacao_meet_1, grau_def_meet_1)
grau_ativacao_join_1 = fuzz.interp_membership(universo, agregacao_join_1, grau_def_join_1)
grau_ativacao_meet_2 = fuzz.interp_membership(universo, agregacao_meet_2, grau_def_meet_2)
grau_ativacao_join_2 = fuzz.interp_membership(universo, agregacao_join_2, grau_def_join_2)
grau_ativacao_meet_10 = fuzz.interp_membership(universo, agregacao_meet_10, grau_def_meet_10)
grau_ativacao_join_10 = fuzz.interp_membership(universo, agregacao_join_10, grau_def_join_10)
grau_ativacao_meet_100 = fuzz.interp_membership(universo, agregacao_meet_100, grau_def_meet_100)
grau_ativacao_join_100 = fuzz.interp_membership(universo, agregacao_join_100, grau_def_join_100)
grau_ativacao_meet_1000 = fuzz.interp_membership(universo, agregacao_meet_1000, grau_def_meet_1000)
grau_ativacao_join_1000 = fuzz.interp_membership(universo, agregacao_join_1000, grau_def_join_1000)

print "grau de amadurecimento kosko: "+str(grau_def_kos)
print "grau de amadurecimento willmott: "+str(grau_def_wil)
print "grau de amadurecimento meet 0.25: "+str(grau_def_meet_025)
print "grau de amadurecimento join 0.25: "+str(grau_def_join_025)
print "grau de amadurecimento meet 0.5: "+str(grau_def_meet_05)
print "grau de amadurecimento join 0.5: "+str(grau_def_join_05)
print "grau de amadurecimento meet 1: "+str(grau_def_meet_1)
print "grau de amadurecimento join 1: "+str(grau_def_join_1)
print "grau de amadurecimento meet 2: "+str(grau_def_meet_2)
print "grau de amadurecimento join 2: "+str(grau_def_join_2)
print "grau de amadurecimento meet 10: "+str(grau_def_meet_10)
print "grau de amadurecimento join 10: "+str(grau_def_join_10)
print "grau de amadurecimento meet 100: "+str(grau_def_meet_100)
print "grau de amadurecimento join 100: "+str(grau_def_join_100)
print "grau de amadurecimento meet 1000: "+str(grau_def_meet_1000)
print "grau de amadurecimento join 1000: "+str(grau_def_join_1000)

fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11), (ax12, ax13, ax14, ax15)) = pl.subplots(4, 4)
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
ax0.fill_between(universo, grau0, agregacao_kos, facecolor='Orange', alpha=0.7)
ax0.plot([grau_def_kos,grau_def_kos], [0, grau_ativacao_kos], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title("Kosko")

ax1.plot(universo, unripeY, 'g--')
ax1.plot(universo, ripeY, 'r--')
ax1.fill_between(universo, grau0, agregacao_wil, facecolor='Orange', alpha=0.7)
ax1.plot([grau_def_wil,grau_def_wil], [0, grau_ativacao_wil], 'k', linewidth=1.5, alpha=0.9)
ax1.set_title("Willmott")

ax2.plot(universo, unripeY, 'g--')
ax2.plot(universo, ripeY, 'r--')
ax2.fill_between(universo, grau0, agregacao_meet_025, facecolor='Orange', alpha=0.7)
ax2.plot([grau_def_meet_025,grau_def_meet_025], [0, grau_ativacao_meet_025], 'k', linewidth=1.5, alpha=0.9)
ax2.set_title("Meet p=0.25")

ax3.plot(universo, unripeY, 'g--')
ax3.plot(universo, ripeY, 'r--')
ax3.fill_between(universo, grau0, agregacao_join_025, facecolor='Orange', alpha=0.7)
ax3.plot([grau_def_join_025,grau_def_join_025], [0, grau_ativacao_join_025], 'k', linewidth=1.5, alpha=0.9)
ax3.set_title("Join p=0.25")

ax4.plot(universo, unripeY, 'g--')
ax4.plot(universo, ripeY, 'r--')
ax4.fill_between(universo, grau0, agregacao_meet_05, facecolor='Orange', alpha=0.7)
ax4.plot([grau_def_meet_05,grau_def_meet_05], [0, grau_ativacao_meet_05], 'k', linewidth=1.5, alpha=0.9)
ax4.set_title("Meet p=0.5")

ax5.plot(universo, unripeY, 'g--')
ax5.plot(universo, ripeY, 'r--')
ax5.fill_between(universo, grau0, agregacao_join_05, facecolor='Orange', alpha=0.7)
ax5.plot([grau_def_join_05,grau_def_join_05], [0, grau_ativacao_join_05], 'k', linewidth=1.5, alpha=0.9)
ax5.set_title("Join p=0.5")

ax6.plot(universo, unripeY, 'g--')
ax6.plot(universo, ripeY, 'r--')
ax6.fill_between(universo, grau0, agregacao_meet_1, facecolor='Orange', alpha=0.7)
ax6.plot([grau_def_meet_1,grau_def_meet_1], [0, grau_ativacao_meet_1], 'k', linewidth=1.5, alpha=0.9)
ax6.set_title("Meet p=1")

ax7.plot(universo, unripeY, 'g--')
ax7.plot(universo, ripeY, 'r--')
ax7.fill_between(universo, grau0, agregacao_join_1, facecolor='Orange', alpha=0.7)
ax7.plot([grau_def_join_1,grau_def_join_1], [0, grau_ativacao_join_1], 'k', linewidth=1.5, alpha=0.9)
ax7.set_title("Join p=1")

ax8.plot(universo, unripeY, 'g--')
ax8.plot(universo, ripeY, 'r--')
ax8.fill_between(universo, grau0, agregacao_meet_2, facecolor='Orange', alpha=0.7)
ax8.plot([grau_def_meet_2,grau_def_meet_2], [0, grau_ativacao_meet_2], 'k', linewidth=1.5, alpha=0.9)
ax8.set_title("Meet p=2")

ax9.plot(universo, unripeY, 'g--')
ax9.plot(universo, ripeY, 'r--')
ax9.fill_between(universo, grau0, agregacao_join_2, facecolor='Orange', alpha=0.7)
ax9.plot([grau_def_join_2,grau_def_join_2], [0, grau_ativacao_join_2], 'k', linewidth=1.5, alpha=0.9)
ax9.set_title("Join p=2")

ax10.plot(universo, unripeY, 'g--')
ax10.plot(universo, ripeY, 'r--')
ax10.fill_between(universo, grau0, agregacao_meet_10, facecolor='Orange', alpha=0.7)
ax10.plot([grau_def_meet_10,grau_def_meet_10], [0, grau_ativacao_meet_10], 'k', linewidth=1.5, alpha=0.9)
ax10.set_title("Meet p=10")

ax11.plot(universo, unripeY, 'g--')
ax11.plot(universo, ripeY, 'r--')
ax11.fill_between(universo, grau0, agregacao_join_10, facecolor='Orange', alpha=0.7)
ax11.plot([grau_def_join_10,grau_def_join_10], [0, grau_ativacao_join_10], 'k', linewidth=1.5, alpha=0.9)
ax11.set_title("Join p=10")

ax12.plot(universo, unripeY, 'g--')
ax12.plot(universo, ripeY, 'r--')
ax12.fill_between(universo, grau0, agregacao_meet_100, facecolor='Orange', alpha=0.7)
ax12.plot([grau_def_meet_100,grau_def_meet_100], [0, grau_ativacao_meet_100], 'k', linewidth=1.5, alpha=0.9)
ax12.set_title("Meet p=100")

ax13.plot(universo, unripeY, 'g--')
ax13.plot(universo, ripeY, 'r--')
ax13.fill_between(universo, grau0, agregacao_join_100, facecolor='Orange', alpha=0.7)
ax13.plot([grau_def_join_100,grau_def_join_100], [0, grau_ativacao_join_100], 'k', linewidth=1.5, alpha=0.9)
ax13.set_title("Join p=100")

ax14.plot(universo, unripeY, 'g--')
ax14.plot(universo, ripeY, 'r--')
ax14.fill_between(universo, grau0, agregacao_meet_1000, facecolor='Orange', alpha=0.7)
ax14.plot([grau_def_meet_1000,grau_def_meet_1000], [0, grau_ativacao_meet_1000], 'k', linewidth=1.5, alpha=0.9)
ax14.set_title("Meet p=1000")

ax15.plot(universo, unripeY, 'g--')
ax15.plot(universo, ripeY, 'r--')
ax15.fill_between(universo, grau0, agregacao_join_1000, facecolor='Orange', alpha=0.7)
ax15.plot([grau_def_join_1000,grau_def_join_1000], [0, grau_ativacao_join_1000], 'k', linewidth=1.5, alpha=0.9)
ax15.set_title("Join p=1000")

pl.tight_layout()
pl.show()
#pl.savefig("resultados/entrada.png")
