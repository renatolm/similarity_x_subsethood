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
c = 5

inpY = []

universo = np.arange(0,10,0.001)

for i in universo:
	inpY.append(membership.triang(i,inp[0],inp[1],inp[2]))

inp_mod = [inp[0]-c, inp[1], inp[2]+c]

inpY_mod = []

for i in universo:
	inpY_mod.append(membership.triang(i,inp_mod[0],inp_mod[1],inp_mod[2]))

#Antecedent membership functions
green = [0.0, 3.0, 4.0]
red = [7.0, 8.0, 10.0]

redY = []
greenY = []
for i in universo:
	redY.append(membership.triang(i,red[0],red[1],red[2]))
	greenY.append(membership.triang(i,green[0],green[1],green[2]))


#Consequent membership functions
unripe = [0.0, 3.0, 4.0]
ripe = [6.0, 7.0, 10.0]

unripeY = []
ripeY = []
for i in universo:
	unripeY.append(membership.triang(i,unripe[0],unripe[1],unripe[2]))
	ripeY.append(membership.triang(i,ripe[0],ripe[1],ripe[2]))

#Rules
#Rule 1: If a tomato is red then the tomato is ripe
regra1_subsethood_kosko = subsethood.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2])
regra1_subsethood_meet_025 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.25)
regra1_subsethood_meet_05 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],0.5)
regra1_subsethood_meet_1 = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp[0],inp[1],inp[2],1)

regra1_subsethood_kosko_mod = subsethood.ativa_regra(red[0],red[1],red[2],inp_mod[0],inp_mod[1],inp_mod[2])
regra1_subsethood_meet_025_mod = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp_mod[0],inp_mod[1],inp_mod[2],0.25)
regra1_subsethood_meet_05_mod = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp_mod[0],inp_mod[1],inp_mod[2],0.5)
regra1_subsethood_meet_1_mod = subsethood_meet_param.ativa_regra(red[0],red[1],red[2],inp_mod[0],inp_mod[1],inp_mod[2],1)

print "ativacao regra 1 kos: "+str(regra1_subsethood_kosko)
print "ativacao regra 1 meet 025: "+str(regra1_subsethood_meet_025)
print "ativacao regra 1 meet 05: "+str(regra1_subsethood_meet_05)
print "ativacao regra 1 meet 1: "+str(regra1_subsethood_meet_1)

print "ativacao regra 1 kos mod: "+str(regra1_subsethood_kosko_mod)
print "ativacao regra 1 meet 025 mod: "+str(regra1_subsethood_meet_025_mod)
print "ativacao regra 1 meet 05 mod: "+str(regra1_subsethood_meet_05_mod)
print "ativacao regra 1 meet 1 mod: "+str(regra1_subsethood_meet_1_mod)

regra1_kos = []
regra1_meet_025 = []
regra1_meet_05 = []
regra1_meet_1 = []
for i in universo:
	regra1_kos.append(np.fmin(regra1_subsethood_kosko,membership.triang(i,ripe[0],ripe[1],ripe[2])))	
	regra1_meet_025.append(np.fmin(regra1_subsethood_meet_025,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_05.append(np.fmin(regra1_subsethood_meet_05,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_1.append(np.fmin(regra1_subsethood_meet_1,membership.triang(i,ripe[0],ripe[1],ripe[2])))

regra1_kos_mod = []
regra1_meet_025_mod = []
regra1_meet_05_mod = []
regra1_meet_1_mod = []
for i in universo:
	regra1_kos_mod.append(np.fmin(regra1_subsethood_kosko_mod,membership.triang(i,ripe[0],ripe[1],ripe[2])))	
	regra1_meet_025_mod.append(np.fmin(regra1_subsethood_meet_025_mod,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_05_mod.append(np.fmin(regra1_subsethood_meet_05_mod,membership.triang(i,ripe[0],ripe[1],ripe[2])))
	regra1_meet_1_mod.append(np.fmin(regra1_subsethood_meet_1_mod,membership.triang(i,ripe[0],ripe[1],ripe[2])))

#Rule 2: If a tomato is green then the tomato is unripe
regra2_subsethood_kosko = subsethood.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2])
regra2_subsethood_meet_025 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.25)
regra2_subsethood_meet_05 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],0.5)
regra2_subsethood_meet_1 = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp[0],inp[1],inp[2],1)

regra2_subsethood_kosko_mod = subsethood.ativa_regra(green[0],green[1],green[2],inp_mod[0],inp_mod[1],inp_mod[2])
regra2_subsethood_meet_025_mod = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp_mod[0],inp_mod[1],inp_mod[2],0.25)
regra2_subsethood_meet_05_mod = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp_mod[0],inp_mod[1],inp_mod[2],0.5)
regra2_subsethood_meet_1_mod = subsethood_meet_param.ativa_regra(green[0],green[1],green[2],inp_mod[0],inp_mod[1],inp_mod[2],1)

print "ativacao regra 2 kos: "+str(regra2_subsethood_kosko)
print "ativacao regra 2 meet 025: "+str(regra2_subsethood_meet_025)
print "ativacao regra 2 meet 05: "+str(regra2_subsethood_meet_05)
print "ativacao regra 2 meet 1: "+str(regra2_subsethood_meet_1)

print "ativacao regra 2 kos mod: "+str(regra2_subsethood_kosko_mod)
print "ativacao regra 2 meet 025 mod: "+str(regra2_subsethood_meet_025_mod)
print "ativacao regra 2 meet 05 mod: "+str(regra2_subsethood_meet_05_mod)
print "ativacao regra 2 meet 1 mod: "+str(regra2_subsethood_meet_1_mod)

regra2_kos = []
regra2_meet_025 = []
regra2_meet_05 = []
regra2_meet_1 = []

for i in universo:
	regra2_kos.append(np.fmin(regra2_subsethood_kosko,membership.triang(i,unripe[0],unripe[1],unripe[2])))	
	regra2_meet_025.append(np.fmin(regra2_subsethood_meet_025,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_05.append(np.fmin(regra2_subsethood_meet_05,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_1.append(np.fmin(regra2_subsethood_meet_1,membership.triang(i,unripe[0],unripe[1],unripe[2])))

regra2_kos_mod = []
regra2_meet_025_mod = []
regra2_meet_05_mod = []
regra2_meet_1_mod = []

for i in universo:
	regra2_kos_mod.append(np.fmin(regra2_subsethood_kosko_mod,membership.triang(i,unripe[0],unripe[1],unripe[2])))	
	regra2_meet_025_mod.append(np.fmin(regra2_subsethood_meet_025_mod,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_05_mod.append(np.fmin(regra2_subsethood_meet_05_mod,membership.triang(i,unripe[0],unripe[1],unripe[2])))
	regra2_meet_1_mod.append(np.fmin(regra2_subsethood_meet_1_mod,membership.triang(i,unripe[0],unripe[1],unripe[2])))

## Agregacao das regras
agregacao_kos = np.fmax(regra1_kos,regra2_kos)
agregacao_meet_025 = np.fmax(regra1_meet_025,regra2_meet_025)
agregacao_meet_05 = np.fmax(regra1_meet_05,regra2_meet_05)
agregacao_meet_1 = np.fmax(regra1_meet_1,regra2_meet_1)

agregacao_kos_mod = np.fmax(regra1_kos_mod,regra2_kos_mod)
agregacao_meet_025_mod = np.fmax(regra1_meet_025_mod,regra2_meet_025_mod)
agregacao_meet_05_mod = np.fmax(regra1_meet_05_mod,regra2_meet_05_mod)
agregacao_meet_1_mod = np.fmax(regra1_meet_1_mod,regra2_meet_1_mod)

grau0 = np.zeros_like(universo)	#variavel auxiliar para montar o grafico

## Calculo do resultado defuzzificado
try:
	grau_def_kos = fuzz.defuzz(universo, agregacao_kos, 'centroid')		#defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_kos = 0

try:
	grau_def_meet_025 = fuzz.defuzz(universo, agregacao_meet_025, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_025 = 0

try:
	grau_def_meet_05 = fuzz.defuzz(universo, agregacao_meet_05, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_05 = 0

try:
	grau_def_meet_1 = fuzz.defuzz(universo, agregacao_meet_1, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_1 = 0

try:
	grau_def_kos_mod = fuzz.defuzz(universo, agregacao_kos_mod, 'centroid')		#defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_kos_mod = 0

try:
	grau_def_meet_025_mod = fuzz.defuzz(universo, agregacao_meet_025_mod, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_025_mod = 0

try:
	grau_def_meet_05_mod = fuzz.defuzz(universo, agregacao_meet_05_mod, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_05_mod = 0

try:
	grau_def_meet_1_mod = fuzz.defuzz(universo, agregacao_meet_1_mod, 'centroid') #defuzzificacao pelo metodo centroide
except AssertionError:
	grau_def_meet_1_mod = 0

grau_ativacao_kos = fuzz.interp_membership(universo, agregacao_kos, grau_def_kos)
grau_ativacao_meet_025 = fuzz.interp_membership(universo, agregacao_meet_025, grau_def_meet_025)
grau_ativacao_meet_05 = fuzz.interp_membership(universo, agregacao_meet_05, grau_def_meet_05)
grau_ativacao_meet_1 = fuzz.interp_membership(universo, agregacao_meet_1, grau_def_meet_1)

grau_ativacao_kos_mod = fuzz.interp_membership(universo, agregacao_kos_mod, grau_def_kos_mod)
grau_ativacao_meet_025_mod = fuzz.interp_membership(universo, agregacao_meet_025_mod, grau_def_meet_025_mod)
grau_ativacao_meet_05_mod = fuzz.interp_membership(universo, agregacao_meet_05_mod, grau_def_meet_05_mod)
grau_ativacao_meet_1_mod = fuzz.interp_membership(universo, agregacao_meet_1_mod, grau_def_meet_1_mod)

print "grau de amadurecimento kosko: "+str(grau_def_kos)
print "grau de amadurecimento meet 0.25: "+str(grau_def_meet_025)
print "grau de amadurecimento meet 0.5: "+str(grau_def_meet_05)
print "grau de amadurecimento meet 1: "+str(grau_def_meet_1)

print "grau de amadurecimento kosko mod: "+str(grau_def_kos_mod)
print "grau de amadurecimento meet 0.25 mod: "+str(grau_def_meet_025_mod)
print "grau de amadurecimento meet 0.5 mod: "+str(grau_def_meet_05_mod)
print "grau de amadurecimento meet 1 mod: "+str(grau_def_meet_1_mod)

fig, ((ax0, ax1, ax2, ax3), (ax4, ax5, ax6, ax7), (ax8, ax9, ax10, ax11), (ax12, ax13, ax14, ax15)) = pl.subplots(4, 4)
#Plot
#pl.plot(universo,greenY,'g--')
#pl.plot(universo,redY, 'r--')
#pl.plot(universo,inpY, 'b')
#pl.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
#pl.fill_between(universo, grau0, agregacao, facecolor='Orange', alpha=0.7)
#pl.plot([grau_def, grau_def], [0, grau_ativacao], 'k', linewidth=1.5, alpha=0.9)
#pl.axis([0, 10, 0, 1])

ax0.plot(universo, greenY, 'g--')
ax0.plot(universo, redY, 'r--')
ax0.plot(universo, inpY, 'b')
ax0.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
ax0.set_title("Entrada")

ax1.plot(universo, unripeY, 'g--')
ax1.plot(universo, ripeY, 'r--')
ax1.fill_between(universo, grau0, agregacao_kos, facecolor='Orange', alpha=0.7)
#ax1.plot([grau_def_kos,grau_def_kos], [0, grau_ativacao_kos], 'k', linewidth=1.5, alpha=0.9)
ax1.set_title("Kosko")

ax2.plot(universo, greenY, 'g--')
ax2.plot(universo, redY, 'r--')
ax2.plot(universo, inpY_mod, 'b')
ax2.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY_mod),np.fmin(redY,inpY_mod)), facecolor='Orange', alpha=0.7)
ax2.set_title("Entrada modificada")

ax3.plot(universo, unripeY, 'g--')
ax3.plot(universo, ripeY, 'r--')
ax3.fill_between(universo, grau0, agregacao_kos_mod, facecolor='Orange', alpha=0.7)
#ax3.plot([grau_def_kos,grau_def_kos_mod], [0, grau_ativacao_kos_mod], 'k', linewidth=1.5, alpha=0.9)
ax3.set_title("Kosko")

ax4.plot(universo, greenY, 'g--')
ax4.plot(universo, redY, 'r--')
ax4.plot(universo, inpY, 'b')
ax4.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
ax4.set_title("Entrada")

ax5.plot(universo, unripeY, 'g--')
ax5.plot(universo, ripeY, 'r--')
ax5.fill_between(universo, grau0, agregacao_meet_025, facecolor='Orange', alpha=0.7)
#ax5.plot([grau_def_meet_025,grau_def_meet_025], [0, grau_ativacao_meet_025], 'k', linewidth=1.5, alpha=0.9)
ax5.set_title("Meet p=0.25")

ax6.plot(universo, greenY, 'g--')
ax6.plot(universo, redY, 'r--')
ax6.plot(universo, inpY_mod, 'b')
ax6.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY_mod),np.fmin(redY,inpY_mod)), facecolor='Orange', alpha=0.7)
ax6.set_title("Entrada modificada")

ax7.plot(universo, unripeY, 'g--')
ax7.plot(universo, ripeY, 'r--')
ax7.fill_between(universo, grau0, agregacao_meet_025_mod, facecolor='Orange', alpha=0.7)
#ax7.plot([grau_def_meet_025_mod,grau_def_meet_025_mod], [0, grau_ativacao_meet_025_mod], 'k', linewidth=1.5, alpha=0.9)
ax7.set_title("Meet p=0.25")

ax8.plot(universo, greenY, 'g--')
ax8.plot(universo, redY, 'r--')
ax8.plot(universo, inpY, 'b')
ax8.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
ax8.set_title("Entrada")

ax9.plot(universo, unripeY, 'g--')
ax9.plot(universo, ripeY, 'r--')
ax9.fill_between(universo, grau0, agregacao_meet_05, facecolor='Orange', alpha=0.7)
#ax9.plot([grau_def_meet_05,grau_def_meet_05], [0, grau_ativacao_meet_05], 'k', linewidth=1.5, alpha=0.9)
ax9.set_title("Meet p=0.5")

ax10.plot(universo, greenY, 'g--')
ax10.plot(universo, redY, 'r--')
ax10.plot(universo, inpY_mod, 'b')
ax10.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY_mod),np.fmin(redY,inpY_mod)), facecolor='Orange', alpha=0.7)
ax10.set_title("Entrada modificada")

ax11.plot(universo, unripeY, 'g--')
ax11.plot(universo, ripeY, 'r--')
ax11.fill_between(universo, grau0, agregacao_meet_05_mod, facecolor='Orange', alpha=0.7)
#ax11.plot([grau_def_meet_05_mod,grau_def_meet_05_mod], [0, grau_ativacao_meet_05_mod], 'k', linewidth=1.5, alpha=0.9)
ax11.set_title("Meet p=0.5")

ax12.plot(universo, greenY, 'g--')
ax12.plot(universo, redY, 'r--')
ax12.plot(universo, inpY, 'b')
ax12.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY),np.fmin(redY,inpY)), facecolor='Orange', alpha=0.7)
ax12.set_title("Entrada")

ax13.plot(universo, unripeY, 'g--')
ax13.plot(universo, ripeY, 'r--')
ax13.fill_between(universo, grau0, agregacao_meet_1, facecolor='Orange', alpha=0.7)
#ax13.plot([grau_def_meet_1,grau_def_meet_1], [0, grau_ativacao_meet_1], 'k', linewidth=1.5, alpha=0.9)
ax13.set_title("Meet p=1")

ax14.plot(universo, greenY, 'g--')
ax14.plot(universo, redY, 'r--')
ax14.plot(universo, inpY_mod, 'b')
ax14.fill_between(universo, grau0, np.fmax(np.fmin(greenY,inpY_mod),np.fmin(redY,inpY_mod)), facecolor='Orange', alpha=0.7)
ax14.set_title("Entrada modificada")

ax15.plot(universo, unripeY, 'g--')
ax15.plot(universo, ripeY, 'r--')
ax15.fill_between(universo, grau0, agregacao_meet_1_mod, facecolor='Orange', alpha=0.7)
#ax15.plot([grau_def_meet_1_mod,grau_def_meet_1_mod], [0, grau_ativacao_meet_1_mod], 'k', linewidth=1.5, alpha=0.9)
ax15.set_title("Meet p=1")

pl.tight_layout()
#pl.show()
pl.savefig("resultados/resultados5_c5.png")
