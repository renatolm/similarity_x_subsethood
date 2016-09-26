from __future__ import division
import numpy as np
import membership

#Tratamento para entradas triangulares e antecedentes triangulares
def ativa_regra(iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	for i in np.arange(iniEntrada, fimEntrada, 0.01):
		if membership.triang(i, iniRegra, topoRegra, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada):
			if grau < membership.triang(i, iniRegra, topoRegra, fimRegra):
				grau = membership.triang(i, iniRegra, topoRegra, fimRegra)

	return grau

#Tratamento para entradas triangulares e antecedentes trapezoidais
def ativa_regra_trap(iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	for i in np.arange(iniEntrada, fimEntrada, 0.01):
		if membership.trap(i, iniRegra, topoRegra1, topoRegra2, fimRegra) >= membership.triang(i, iniEntrada, topoEntrada, fimEntrada):
			if grau < membership.triang(i, iniEntrada, topoEntrada, fimEntrada):
				grau = membership.triang(i, iniEntrada, topoEntrada, fimEntrada)

	return grau

#Tratamento para entradas crisp e antecedentes triangulares
def ativa_regra_crisp(iniRegra, topoRegra, fimRegra, entrada):
	grau = membership.triang(entrada,iniRegra,topoRegra,fimRegra)

	return grau

#Tratamento para entradas crisp e antecedentes triangulares
def ativa_regra_trap_crisp(iniRegra, topoRegra1, topoRegra2, fimRegra, entrada):
	grau = membership.trap(entrada,iniRegra,topoRegra1,topoRegra2,fimRegra)

	return grau