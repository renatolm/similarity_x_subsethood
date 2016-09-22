from __future__ import division
import numpy as np
import membership
import scipy.integrate as integrate

# Calcula a similaridade de Jaccard
# A similaridade eh dada por Integral(min(antecedente,entrada))/Integral(max(antecedente,entrada))
# O intervalo de integracao eh dividido em tuplas e armazenado no array intervalos
# A estrutura de cada tupla eh a seguinte: [funcao, inicio, fim]
# Onde funcao indica quem tem o menor valor em modulo no intervalo (antecedente ou entrada)

def ativa_regra(iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	numerador = 0
	denominador = 0
	intervalosNum = []
	intervalosDen = []

	# Nao ha interseccao entre a entrada e o antecedente
	if max(iniEntrada,iniRegra) >= min(fimEntrada,fimRegra):
		return 0

	# Determina quem eh menor no inicio do intervalo: o antecedente ou a entrada
	if membership.triang(max(iniEntrada,iniRegra), iniRegra, topoRegra, fimRegra) >= membership.triang(max(iniEntrada,iniRegra), iniEntrada, topoEntrada, fimEntrada):
		intervalo = ['entrada',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]
	else:
		intervalo = ['antecedente',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]

	#Monta os intervalos de integracao do numerador em tuplas no array intervalosNum
	for i in np.arange(max(iniEntrada,iniRegra), min(fimEntrada,fimRegra), 0.01):		
		if (membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalo[2] = i
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalosNum.append(intervalo)
			intervalo = ['entrada',i,i]
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalosNum.append(intervalo)
			intervalo = ['antecedente',i,i]
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalo[2] = i

	intervalosNum.append(intervalo)


	# Determina quem eh maior no inicio do intervalo: o antecedente ou a entrada
	if membership.triang(max(iniEntrada,iniRegra), iniRegra, topoRegra, fimRegra) >= membership.triang(max(iniEntrada,iniRegra), iniEntrada, topoEntrada, fimEntrada):
		intervalo = ['antecedente',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]
	else:
		intervalo = ['entrada',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]

	#Monta os intervalos de integracao do denominador em tuplas no array intervalosDen
	for i in np.arange(min(iniEntrada,iniRegra), max(fimEntrada,fimRegra), 0.01):
		if (membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalosDen.append(intervalo)
			intervalo = ['antecedente',i,i]			
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalo[2] = i
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalo[2] = i
		elif (membership.triang(i, iniRegra, topoRegra, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalosNum.append(intervalo)
			intervalo = ['entrada',i,i]		
			
	intervalosDen.append(intervalo)	

	# Integra os intervalos definidos para o numerador
	for intervalo in intervalosNum:
		if intervalo[0] == 'antecedente':
			numerador = numerador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniRegra,topoRegra,fimRegra))[0]
		else:
			numerador = numerador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniEntrada,topoEntrada,fimEntrada))[0]

	# Integra os intervalos definidos para o denominador
	for intervalo in intervalosDen:
		if intervalo[0] == 'antecedente':
			denominador = denominador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniRegra,topoRegra,fimRegra))[0]
		else:
			denominador = denominador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniEntrada,topoEntrada,fimEntrada))[0]

	# Calcula o grau de similaridade
	grau = numerador / denominador
	return grau

def ativa_regra_trap(iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	numerador = 0
	denominador = 0
	intervalosNum = []
	intervalosDen = []

	# Nao ha interseccao entre a entrada e o antecedente
	if max(iniEntrada,iniRegra) >= min(fimEntrada,fimRegra):
		return 0

	# Determina quem eh menor no inicio do intervalo: o antecedente ou a entrada
	if membership.trap(max(iniEntrada,iniRegra), iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(max(iniEntrada,iniRegra), iniEntrada, topoEntrada, fimEntrada):
		intervalo = ['entrada',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]
	else:
		intervalo = ['antecedente',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]

	#Monta os intervalos de integracao do numerador em tuplas no array intervalosNum
	for i in np.arange(max(iniEntrada,iniRegra), min(fimEntrada,fimRegra), 0.01):		
		if (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalo[2] = i
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalosNum.append(intervalo)
			intervalo = ['entrada',i,i]
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalosNum.append(intervalo)
			intervalo = ['antecedente',i,i]
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalo[2] = i

	intervalosNum.append(intervalo)


	# Determina quem eh maior no inicio do intervalo: o antecedente ou a entrada
	if membership.trap(max(iniEntrada,iniRegra), iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(max(iniEntrada,iniRegra), iniEntrada, topoEntrada, fimEntrada):
		intervalo = ['antecedente',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]
	else:
		intervalo = ['entrada',max(iniEntrada,iniRegra),max(iniEntrada,iniRegra)]

	#Monta os intervalos de integracao do denominador em tuplas no array intervalosDen
	for i in np.arange(min(iniEntrada,iniRegra), max(fimEntrada,fimRegra), 0.01):
		if (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalosDen.append(intervalo)
			intervalo = ['antecedente',i,i]			
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalo[2] = i
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'entrada'):
			intervalo[2] = i
		elif (membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) <= membership.triang(i, iniEntrada, topoEntrada, fimEntrada)) and (intervalo[0] == 'antecedente'):
			intervalosNum.append(intervalo)
			intervalo = ['entrada',i,i]		
			
	intervalosDen.append(intervalo)	

	# Integra os intervalos definidos para o numerador
	for intervalo in intervalosNum:
		if intervalo[0] == 'antecedente':
			numerador = numerador + integrate.quad(membership.trap, intervalo[1], intervalo[2], args=(iniRegra,topoRegra1,topoRegra2,fimRegra))[0]
		else:
			numerador = numerador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniEntrada,topoEntrada,fimEntrada))[0]

	# Integra os intervalos definidos para o denominador
	for intervalo in intervalosDen:
		if intervalo[0] == 'antecedente':
			denominador = denominador + integrate.quad(membership.trap, intervalo[1], intervalo[2], args=(iniRegra,topoRegra1,topoRegra2,fimRegra))[0]
		else:
			denominador = denominador + integrate.quad(membership.triang, intervalo[1], intervalo[2], args=(iniEntrada,topoEntrada,fimEntrada))[0]

	# Calcula o grau de similaridade
	grau = numerador / denominador
	return grau