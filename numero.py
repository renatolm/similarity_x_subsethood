import numpy as np
import pylab as pl

import membership

def centralize(inp, universo):
	inpY = []
	for i in universo:
		inpY.append(membership.triang(i,inp[0]-inp[1],inp[1]-inp[1],inp[2]-inp[1]))

	return inpY


#Input
inp = [2.0,3.0,4.0]

inpY = []

universo = np.arange(-10,10,0.001)

inpY = centralize(inp, universo)

pl.plot(universo,inpY, 'b')
pl.axis([-10, 10, 0, 1])
pl.savefig("numero_center.png")
