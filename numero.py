from __future__ import division
import numpy as np
import pylab as pl

import membership

def centralize(inp, universo):
	inpY = []
	for i in universo:
		inpY.append(membership.triang(i,inp[0]-inp[1],inp[1]-inp[1],inp[2]-inp[1]))

	return inpY

def getNumberFromAlphaCut(universo):
	a = np.zeros((len(universo),),float)
	for alpha in np.arange(0,1,0.001):
		pos = 0
		for i in universo:
			if (i>(2/5*alpha + 4/5)) and (i<(-4*alpha + 16)):
				a[pos] = alpha
			pos = pos+1

	return a

#Input
inp = [2.0,3.0,4.0]

inpY = []

universo = np.arange(0,20,0.001)

#inpY = centralize(inp, universo)
inpY = getNumberFromAlphaCut(universo)

pl.plot(universo,inpY, 'b')
pl.axis([0, 20, 0, 1.1])
pl.savefig("numero_resultado.png")
#pl.show()
