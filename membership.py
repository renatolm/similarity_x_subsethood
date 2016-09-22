from __future__ import division

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