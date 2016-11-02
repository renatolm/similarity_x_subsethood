from __future__ import division
import numpy as np
import membership
import scipy.integrate as integrate

# Calcula a medida de subsethood de Wilmot
# A similaridade eh dada por Integral(antecedente)/Integral(max(entrada,antecedente))
# O intervalo de integracao eh dividido em tuplas e armazenado no array intervalos
# A estrutura de cada tupla eh a seguinte: [funcao, inicio, fim]
# Onde funcao indica quem tem o maior valor em modulo no intervalo (antecedente ou entrada)

def ativa_regra(iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	numerador = 0
	denominador = 0
	#intervalosNum = []
	intervalosDen = []

	# Determina quem eh maior no inicio do intervalo: o antecedente ou a entrada
	if membership.triang(min(iniEntrada,iniRegra), iniRegra, topoRegra, fimRegra) <= membership.triang(min(iniEntrada,iniRegra), iniEntrada, topoEntrada, fimEntrada):
		intervalo = ['entrada',min(iniEntrada,iniRegra),min(iniEntrada,iniRegra)]
	else:
		intervalo = ['antecedente',min(iniEntrada,iniRegra),min(iniEntrada,iniRegra)]

	#Monta os intervalos de integracao do denominador em tuplas no array intervalosDen
	for i in np.arange(min(iniEntrada,iniRegra), max(fimEntrada,fimRegra), 0.001):		
		if (membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalo[2] = i
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalosDen.append(intervalo)
			intervalo = ['antecedente',i,i]
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalosDen.append(intervalo)
			intervalo = ['entrada',i,i]
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalo[2] = i

	intervalosDen.append(intervalo)
	

	# Integra os intervalos definidos para o denominador
	for intervalo in intervalosDen:
		if intervalo[0] == 'antecedente':
			denominador = denominador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniRegra,topoRegra,fimRegra))[0]
		else:
			denominador = denominador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniEntrada,topoEntrada,fimEntrada))[0]


	numerador = integrate.quad(membership.triang, iniRegra, fimRegra, args=(iniRegra,topoRegra,fimRegra))[0]
	# Calcula o grau de similaridade
	grau = numerador / denominador
	return grau

def ativa_regra_trap(iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	numerador = 0
	denominador = 0
	# intervalosNum = []
	intervalosDen = []

	# Determina quem eh maior no inicio do intervalo: o antecedente ou a entrada
	if membership.trap(min(iniEntrada,iniRegra), iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(min(iniEntrada,iniRegra), iniEntrada, topoEntrada, fimEntrada):
		intervalo = ['entrada',min(iniEntrada,iniRegra),min(iniEntrada,iniRegra)]
	else:
		intervalo = ['antecedente',min(iniEntrada,iniRegra),min(iniEntrada,iniRegra)]

	#Monta os intervalos de integracao do denominador em tuplas no array intervalosDen
	for i in np.arange(min(iniEntrada,iniRegra), max(fimEntrada,fimRegra), 0.001):		
		if (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalo[2] = i
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalosDen.append(intervalo)
			intervalo = ['antecedente',i,i]
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalosDen.append(intervalo)
			intervalo = ['entrada',i,i]
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalo[2] = i

	intervalosDen.append(intervalo)
	

	# Integra os intervalos definidos para o denominador
	for intervalo in intervalosDen:
		if intervalo[0] == 'antecedente':
			denominador = denominador + integrate.quad(membership.trap, intervalo[1], intervalo[2], args=(iniRegra,topoRegra1, topoRegra2,fimRegra))[0]
		else:
			denominador = denominador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniEntrada,topoEntrada,fimEntrada))[0]


	numerador = integrate.quad(membership.trap, iniRegra, fimRegra, args=(iniRegra,topoRegra1,topoRegra2,fimRegra))[0]
	# Calcula o grau de similaridade
	grau = numerador / denominador
	return grau
