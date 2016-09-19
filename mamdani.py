from __future__ import division
import numpy as np
import membership

def ativa_regra(iniRegra, topoRegra, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	for i in np.arange(iniEntrada, fimEntrada, 0.01):
		if membership.triang(iniRegra, topoRegra, fimRegra, i) >= membership.triang(iniEntrada, topoEntrada, fimEntrada, i):
			if grau < membership.triang(iniRegra, topoRegra, fimRegra, i):
				grau = membership.triang(iniRegra, topoRegra, fimRegra, i)

	return grau

def ativa_regra_trap(iniRegra, topoRegra1, topoRegra2, fimRegra, iniEntrada, topoEntrada, fimEntrada):
	grau = 0
	for i in np.arange(iniEntrada, fimEntrada, 0.01):
		if membership.trap(iniRegra, topoRegra1, topoRegra2, fimRegra, i) >= membership.triang(iniEntrada, topoEntrada, fimEntrada, i):
			if grau < membership.triang(iniEntrada, topoEntrada, fimEntrada, i):
				grau = membership.triang(iniEntrada, topoEntrada, fimEntrada, i)

	return grau