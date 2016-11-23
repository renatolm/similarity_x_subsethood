from __future__ import division
import numpy as np
import membership
import math

# Calcula a medida de subsethood meet parametrizada
# A similaridade eh dada por vp(min(antecedente,entrada))/vp(entrada)
# Onde vp eh definida como vp(C) = sum((1-cos(pi*[uC(x)]^p)/k)
# com o somatorio variando de 1 ate k, onde k eh o numero de pontos do intervalo

def ativa_regra(iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada, p):
	grau = 0
	numerador = 0
	denominador = 0

	# Nao ha interseccao entre a entrada e o antecedente
	if max(iniEntrada,iniRegra) >= min(fimEntrada,fimRegra):
		return 0	

	#Calcula os somatorios do numerador e do denominador
	for i in np.arange(max(iniEntrada,iniRegra), min(fimEntrada,fimRegra), 0.001):		
		mi = min(membership.triang(i, iniRegra, topoRegra, fimRegra), membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) 
		numerador = numerador + (1 - math.cos(math.pi*((mi)**p)))

	for i in np.arange(iniEntrada, fimEntrada, 0.001):
		entrada = membership.triang(i, iniEntrada, topoEntrada, fimEntrada)
		denominador = denominador + (1 - math.cos(math.pi*((entrada)**p)))

	# Calcula o grau de subsethood
	grau = numerador / denominador
	return grau

def ativa_regra_trap(iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada, p):
	grau = 0
	numerador = 0
	denominador = 0

	# Nao ha interseccao entre a entrada e o antecedente
	if max(iniEntrada,iniRegra) >= min(fimEntrada,fimRegra):
		return 0	

	#Calcula os somatorios do numerador e do denominador
	for i in np.arange(max(iniEntrada,iniRegra), min(fimEntrada,fimRegra), 0.001):		
		mi = min(membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra), membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) 
		numerador = numerador + (1 - math.cos(math.pi*((mi)**p)))

		for i in np.arange(iniEntrada, fimEntrada, 0.001):
		entrada = membership.triang(i, iniEntrada, topoEntrada, fimEntrada)
		denominador = denominador + (1 - math.cos(math.pi*((entrada)**p)))

	# Calcula o grau de subsethood
	grau = numerador / denominador
	return grau
