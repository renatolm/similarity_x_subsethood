from __future__ import division
import numpy as np

def triang(entrada, ini, topo, fim):
	if (entrada > ini) and (entrada < topo):
		return (entrada / (topo - ini)) - (ini / (topo - ini))
	elif (entrada > topo) and (entrada < fim):
		return (-entrada / (fim - topo)) + (fim / (fim - topo))
	elif entrada == topo:
		return 1
	else:
		return 0

def trap(entrada, ini, topo1, topo2, fim):
	if (entrada > ini) and (entrada < topo1):
		return (entrada / (topo1 - ini)) - (ini / (topo1 - ini))
	elif (entrada > topo2) and (entrada < fim):
		return (-entrada / (fim - topo2)) + (fim / (fim - topo2))
	elif (entrada >= topo1) and (entrada <= topo2):
		return 1
	else:
		return 0

def alpha_cut_triang(alpha, ini, topo, fim):
	corte = []
	for i in np.arange(ini, fim, 0.1):
		if triang(i, ini, topo, fim) >= alpha:
			corte.append(i)

	return corte

def alpha_cut_trap(alpha, ini, topo1, topo2, fim):
	corte = []
	for i in np.arange(ini, fim, 0.1):
		if trap(i, ini, topo1, topo2, fim) >= alpha:
			corte.append(i)

	return corte