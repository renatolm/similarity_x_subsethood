from __future__ import division
import numpy as np
import membership
import scipy.integrate as integrate

# Calcula a inclusao sigma-meet de Vassilis
# A inclusao eh dada por Integral_0^1(V(interseccao(entrada,antecedente))/V(entrada))
# Onde V eh uma funcao de comprimento dada por V(A) = v(theta(a1)) + v(a2), A=[a1,a2], v(x) = x e theta(x) = 10 - x
# O intervalo de integracao eh dividido em tuplas e armazenado no array intervalos
# A estrutura de cada tupla eh a seguinte: [funcao, inicio, fim]
# Onde funcao indica quem tem o menor valor em modulo no intervalo (antecedente ou entrada)

def integrand_triang(h, iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	a1 = membership.alpha_cut_triang(h, iniEntrada, topoEntrada, fimEntrada)[0]
	a2 = membership.alpha_cut_triang(h, iniEntrada, topoEntrada, fimEntrada)[-1]
	b1 = membership.alpha_cut_triang(h, iniRegra, topoRegra, fimRegra)[0]
	b2 = membership.alpha_cut_triang(h, iniRegra, topoRegra, fimRegra)[-1]

	numerador = 10 + min(a2,b2) - max(a1,b1)
	denominador = 10 + a2 - a1

	return numerador/denominador

def integrand_trap(h, iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	a1 = membership.alpha_cut_triang(h, iniEntrada, topoEntrada, fimEntrada)[0]
	a2 = membership.alpha_cut_triang(h, iniEntrada, topoEntrada, fimEntrada)[-1]
	b1 = membership.alpha_cut_trap(h, iniRegra, topoRegra1, topoRegra2, fimRegra)[0]
	b2 = membership.alpha_cut_trap(h, iniRegra, topoRegra1, topoRegra2, fimRegra)[-1]

	numerador = 10 + min(a2,b2) - max(a1,b1)
	denominador = 10 + a2 - a1

	return numerador/denominador

def ativa_regra(iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0	

	# Nao ha interseccao entre a entrada e o antecedente
	if max(iniEntrada,iniRegra) >= min(fimEntrada,fimRegra):
		return 0

	# Calcula o grau de inclusao
	grau = integrate.quad(integrand_triang, 0, 1, args=(iniRegra,topoRegra,fimRegra,iniEntrada,topoEntrada,fimEntrada),limit=10000)[0]
	
	return grau

def ativa_regra_trap(iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0	

	# Nao ha interseccao entre a entrada e o antecedente
	if max(iniEntrada,iniRegra) >= min(fimEntrada,fimRegra):
		return 0

	# Calcula o grau de inclusao
	grau = integrate.quad(integrand_trap, 0, 1, args=(iniRegra,topoRegra1,topoRegra2,fimRegra,iniEntrada,topoEntrada,fimEntrada),limit=10000)[0]
	
	return grau