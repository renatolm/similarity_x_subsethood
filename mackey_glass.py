import numpy as np
import pylab as pl
from pydelay import dde23
import mamdani
import similarity
import sigma_meet
import subsethood
import itertools
import math

# define the equations
eqns = {
    'x' : '0.2 * x(t-tau) / (1.0 + pow(x(t-tau),p)) -0.1*x'
    }

#define the parameters
params = {
    'tau': 30,
    'p'  : 10
    }

# Initialise the solver
dde = dde23(eqns=eqns, params=params)

# set the simulation parameters
# (solve from t=0 to t=1000 and limit the maximum step size to 1.0)
dde.set_sim_params(tfinal=1000, dtmax=1.0)

# set the history of to the constant function 0.5 (using a python lambda function)
histfunc = {
    'x': lambda t: 0.6
    }
dde.hist_from_funcs(histfunc, 1000)

# run the simulator
dde.run()

# Make a plot of x(t) vs x(t-tau):
# Sample the solution twice with a stepsize of dt=0.1:

# once in the interval [515, 1000]
#sol1 = dde.sample(515, 1000, 0.1)
#x1 = sol1['x']

# and once between [500, 1000-15]
#sol2 = dde.sample(500, 1000-15, 0.1)
#x2 = sol2['x']

sol1 = dde.sample(0, 1000, 1)
x1 = sol1['x']

#defining membership functions
S3 = [0.0,0.0,0.3,0.5]
S2 = [0.3,0.5,0.7]
S1 = [0.5,0.7,0.9]
CE = [0.7,0.9,1.1]
B1 = [0.9,1.1,1.3]
B2 = [1.1,1.3,1.5]
B3 = [1.3,1.5,1.9,1.9]

#begining Wang-Mendel Algorithm to extract a Fuzzy Rule Base (mamdani)
baseDeRegras = []		#Rule format: [ant1, ant2, ant3, ant4, ant5, ant6, ant7, cons, degree]
						#where ant = antecedent, cons = consequente, degree = product of firing degrees

baseDeRegrasFinal = []

for i in range(0,694,1):
	novaRegra = []
	degree = 1
	for j in range(0,8):	#7 ant -> 1 cons		
		grau = mamdani.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)
		ant = 'S3'

		novo_grau = mamdani.ativa_regra(S2[0], S2[1], S2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S2'
			grau = novo_grau

		novo_grau = mamdani.ativa_regra(S1[0], S1[1], S1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S1'
			grau = novo_grau

		novo_grau = mamdani.ativa_regra(CE[0], CE[1], CE[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'CE'
			grau = novo_grau

		novo_grau = mamdani.ativa_regra(B1[0], B1[1], B1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B1'
			grau = novo_grau

		novo_grau = mamdani.ativa_regra(B2[0], B2[1], B2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B2'
			grau = novo_grau

		novo_grau = mamdani.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B3'
			grau = novo_grau

		degree = degree*grau
		novaRegra.append(ant)

	novaRegra.append(degree)

	for n, regra in enumerate(baseDeRegrasFinal):
		if (regra[0]==novaRegra[0]) and (regra[1]==novaRegra[1]) and (regra[2]==novaRegra[2]) and \
			(regra[3]==novaRegra[3]) and (regra[4]==novaRegra[4]) and (regra[5]==novaRegra[5]) and \
			(regra[6]==novaRegra[6]):			
			if regra[8] > novaRegra[8]:				
				continue				
			else:										
				baseDeRegrasFinal.remove(regra)		

	baseDeRegras.append(novaRegra)
	baseDeRegrasFinal.append(novaRegra)

	if i == 0:		
		baseDeRegrasFinal.append(novaRegra)	

print "tamanho da base de regras original (mamdani): "+str(len(baseDeRegras))
print "tamanho da base de regras reduzida (mamdani): "+str(len(baseDeRegrasFinal))

#Prediction of new inputs (mamdani)
x = []
for k in range(694,994):

	#Determine which rules will be activated for a new input
	ativadas = []

	antecedents = []
	for i in range(0,7):	#determine the antecedents
		antecedent = []
		grau = mamdani.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S3')

		grau = mamdani.ativa_regra(S2[0], S2[1], S2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S2')			

		grau = mamdani.ativa_regra(S1[0], S1[1], S1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S1')			

		grau = mamdani.ativa_regra(CE[0], CE[1], CE[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('CE')		

		grau = mamdani.ativa_regra(B1[0], B1[1], B1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B1')

		grau = mamdani.ativa_regra(B2[0], B2[1], B2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B2')

		grau = mamdani.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B3')

		antecedents.append(antecedent)

	#print antecedents
	combinations = list(itertools.product(*antecedents))

	for i in range(0, len(combinations)):
		for j in range(0, len(baseDeRegrasFinal)):
			if (combinations[i][0]==baseDeRegrasFinal[j][0]) and (combinations[i][1]==baseDeRegrasFinal[j][1]) and (combinations[i][2]==baseDeRegrasFinal[j][2]) and \
				(combinations[i][3]==baseDeRegrasFinal[j][3]) and (combinations[i][4]==baseDeRegrasFinal[j][4]) and (combinations[i][5]==baseDeRegrasFinal[j][5]) and \
				(combinations[i][6]==baseDeRegrasFinal[j][6]):	
				ativadas.append(baseDeRegrasFinal[j])

	#print "quantas ativadas? "+str(len(ativadas))
	#print ativadas
	numerador = []
	denominador = []
	for i in range(0, len(ativadas)):
		prod = 1
		for j in range(0,7):		
			if ativadas[i][j] == 'S3':
				prod = prod * mamdani.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S2':
				prod = prod * mamdani.ativa_regra(S2[0], S2[1], S2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S1':
				prod = prod * mamdani.ativa_regra(S1[0], S1[1], S1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'CE':
				prod = prod * mamdani.ativa_regra(CE[0], CE[1], CE[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B1':
				prod = prod * mamdani.ativa_regra(B1[0], B1[1], B1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B2':
				prod = prod * mamdani.ativa_regra(B2[0], B2[1], B2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B3':
				prod = prod * mamdani.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
		
		if ativadas[i][7] == 'S3':
			num = prod * 0
		elif ativadas[i][7] == 'S2':
			num = prod * 0.5
		elif ativadas[i][7] == 'S1':
			num = prod * 0.7
		elif ativadas[i][7] == 'CE':
			num = prod * 0.9
		elif ativadas[i][7] == 'B1':
			num = prod * 1.1
		elif ativadas[i][7] == 'B2':
			num = prod * 1.3
		elif ativadas[i][7] == 'B3':
			num = prod * 1.5

		numerador.append(num)
		denominador.append(prod)

	#x = sum(numerador)/sum(denominador)
	x.append(sum(numerador)/sum(denominador))

######################################################################################################

#begining Wang-Mendel Algorithm to extract a Fuzzy Rule Base (similarity)
baseDeRegras = []		#Rule format: [ant1, ant2, ant3, ant4, ant5, ant6, ant7, cons, degree]
						#where ant = antecedent, cons = consequente, degree = product of firing degrees

baseDeRegrasFinal = []

for i in range(0,694,1):
	novaRegra = []
	degree = 1
	for j in range(0,8):	#7 ant -> 1 cons		
		grau = similarity.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)
		ant = 'S3'

		novo_grau = similarity.ativa_regra(S2[0], S2[1], S2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S2'
			grau = novo_grau

		novo_grau = similarity.ativa_regra(S1[0], S1[1], S1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S1'
			grau = novo_grau

		novo_grau = similarity.ativa_regra(CE[0], CE[1], CE[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'CE'
			grau = novo_grau

		novo_grau = similarity.ativa_regra(B1[0], B1[1], B1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B1'
			grau = novo_grau

		novo_grau = similarity.ativa_regra(B2[0], B2[1], B2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B2'
			grau = novo_grau

		novo_grau = similarity.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B3'
			grau = novo_grau

		degree = degree*grau
		novaRegra.append(ant)

	novaRegra.append(degree)

	for n, regra in enumerate(baseDeRegrasFinal):
		if (regra[0]==novaRegra[0]) and (regra[1]==novaRegra[1]) and (regra[2]==novaRegra[2]) and \
			(regra[3]==novaRegra[3]) and (regra[4]==novaRegra[4]) and (regra[5]==novaRegra[5]) and \
			(regra[6]==novaRegra[6]):			
			if regra[8] > novaRegra[8]:				
				continue				
			else:										
				baseDeRegrasFinal.remove(regra)		

	baseDeRegras.append(novaRegra)
	baseDeRegrasFinal.append(novaRegra)

	if i == 0:		
		baseDeRegrasFinal.append(novaRegra)	

print "tamanho da base de regras original (similarity): "+str(len(baseDeRegras))
print "tamanho da base de regras reduzida (similarity): "+str(len(baseDeRegrasFinal))

#Prediction of new inputs (similarity)
x3 = []
for k in range(694,994):

	#Determine which rules will be activated for a new input
	ativadas = []

	antecedents = []
	for i in range(0,7):	#determine the antecedents
		antecedent = []
		grau = similarity.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S3')

		grau = similarity.ativa_regra(S2[0], S2[1], S2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S2')			

		grau = similarity.ativa_regra(S1[0], S1[1], S1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S1')			

		grau = similarity.ativa_regra(CE[0], CE[1], CE[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('CE')		

		grau = similarity.ativa_regra(B1[0], B1[1], B1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B1')

		grau = similarity.ativa_regra(B2[0], B2[1], B2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B2')

		grau = similarity.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B3')

		antecedents.append(antecedent)

	#print antecedents
	combinations = list(itertools.product(*antecedents))

	for i in range(0, len(combinations)):
		for j in range(0, len(baseDeRegrasFinal)):
			if (combinations[i][0]==baseDeRegrasFinal[j][0]) and (combinations[i][1]==baseDeRegrasFinal[j][1]) and (combinations[i][2]==baseDeRegrasFinal[j][2]) and \
				(combinations[i][3]==baseDeRegrasFinal[j][3]) and (combinations[i][4]==baseDeRegrasFinal[j][4]) and (combinations[i][5]==baseDeRegrasFinal[j][5]) and \
				(combinations[i][6]==baseDeRegrasFinal[j][6]):	
				ativadas.append(baseDeRegrasFinal[j])

	#print "quantas ativadas? "+str(len(ativadas))
	#print ativadas
	numerador = []
	denominador = []
	for i in range(0, len(ativadas)):
		prod = 1
		for j in range(0,7):		
			if ativadas[i][j] == 'S3':
				prod = prod * similarity.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S2':
				prod = prod * similarity.ativa_regra(S2[0], S2[1], S2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S1':
				prod = prod * similarity.ativa_regra(S1[0], S1[1], S1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'CE':
				prod = prod * similarity.ativa_regra(CE[0], CE[1], CE[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B1':
				prod = prod * similarity.ativa_regra(B1[0], B1[1], B1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B2':
				prod = prod * similarity.ativa_regra(B2[0], B2[1], B2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B3':
				prod = prod * similarity.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
		
		if ativadas[i][7] == 'S3':
			num = prod * 0
		elif ativadas[i][7] == 'S2':
			num = prod * 0.5
		elif ativadas[i][7] == 'S1':
			num = prod * 0.7
		elif ativadas[i][7] == 'CE':
			num = prod * 0.9
		elif ativadas[i][7] == 'B1':
			num = prod * 1.1
		elif ativadas[i][7] == 'B2':
			num = prod * 1.3
		elif ativadas[i][7] == 'B3':
			num = prod * 1.5

		numerador.append(num)
		denominador.append(prod)

	#x = sum(numerador)/sum(denominador)
	x3.append(sum(numerador)/sum(denominador))

#######################################################################################################

#begining Wang-Mendel Algorithm to extract a Fuzzy Rule Base (sigma-meet)
baseDeRegras = []		#Rule format: [ant1, ant2, ant3, ant4, ant5, ant6, ant7, cons, degree]
						#where ant = antecedent, cons = consequente, degree = product of firing degrees

baseDeRegrasFinal = []

for i in range(0,694,1):	
	novaRegra = []
	degree = 1
	for j in range(0,8):	#7 ant -> 1 cons		
		grau = sigma_meet.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)
		ant = 'S3'

		novo_grau = sigma_meet.ativa_regra(S2[0], S2[1], S2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S2'
			grau = novo_grau

		novo_grau = sigma_meet.ativa_regra(S1[0], S1[1], S1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S1'
			grau = novo_grau

		novo_grau = sigma_meet.ativa_regra(CE[0], CE[1], CE[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'CE'
			grau = novo_grau

		novo_grau = sigma_meet.ativa_regra(B1[0], B1[1], B1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B1'
			grau = novo_grau

		novo_grau = sigma_meet.ativa_regra(B2[0], B2[1], B2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B2'
			grau = novo_grau

		novo_grau = sigma_meet.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B3'
			grau = novo_grau

		degree = degree*grau
		novaRegra.append(ant)

	novaRegra.append(degree)

	for n, regra in enumerate(baseDeRegrasFinal):
		if (regra[0]==novaRegra[0]) and (regra[1]==novaRegra[1]) and (regra[2]==novaRegra[2]) and \
			(regra[3]==novaRegra[3]) and (regra[4]==novaRegra[4]) and (regra[5]==novaRegra[5]) and \
			(regra[6]==novaRegra[6]):			
			if regra[8] > novaRegra[8]:				
				continue				
			else:										
				baseDeRegrasFinal.remove(regra)		

	baseDeRegras.append(novaRegra)
	baseDeRegrasFinal.append(novaRegra)

	if i == 0:		
		baseDeRegrasFinal.append(novaRegra)	

print "tamanho da base de regras original (sigma-meet): "+str(len(baseDeRegras))
print "tamanho da base de regras reduzida (sigma-meet): "+str(len(baseDeRegrasFinal))

#Prediction of new inputs (sigma-meet)
x4 = []
for k in range(694,994):

	#Determine which rules will be activated for a new input
	ativadas = []

	antecedents = []
	for i in range(0,7):	#determine the antecedents
		antecedent = []
		grau = sigma_meet.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S3')

		grau = sigma_meet.ativa_regra(S2[0], S2[1], S2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S2')			

		grau = sigma_meet.ativa_regra(S1[0], S1[1], S1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S1')			

		grau = sigma_meet.ativa_regra(CE[0], CE[1], CE[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('CE')		

		grau = sigma_meet.ativa_regra(B1[0], B1[1], B1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B1')

		grau = sigma_meet.ativa_regra(B2[0], B2[1], B2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B2')

		grau = sigma_meet.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B3')

		antecedents.append(antecedent)

	#print antecedents
	combinations = list(itertools.product(*antecedents))

	for i in range(0, len(combinations)):
		for j in range(0, len(baseDeRegrasFinal)):
			if (combinations[i][0]==baseDeRegrasFinal[j][0]) and (combinations[i][1]==baseDeRegrasFinal[j][1]) and (combinations[i][2]==baseDeRegrasFinal[j][2]) and \
				(combinations[i][3]==baseDeRegrasFinal[j][3]) and (combinations[i][4]==baseDeRegrasFinal[j][4]) and (combinations[i][5]==baseDeRegrasFinal[j][5]) and \
				(combinations[i][6]==baseDeRegrasFinal[j][6]):	
				ativadas.append(baseDeRegrasFinal[j])

	#print "quantas ativadas? "+str(len(ativadas))
	#print ativadas
	numerador = []
	denominador = []
	for i in range(0, len(ativadas)):
		prod = 1
		for j in range(0,7):		
			if ativadas[i][j] == 'S3':
				prod = prod * sigma_meet.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S2':
				prod = prod * sigma_meet.ativa_regra(S2[0], S2[1], S2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S1':
				prod = prod * sigma_meet.ativa_regra(S1[0], S1[1], S1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'CE':
				prod = prod * sigma_meet.ativa_regra(CE[0], CE[1], CE[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B1':
				prod = prod * sigma_meet.ativa_regra(B1[0], B1[1], B1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B2':
				prod = prod * sigma_meet.ativa_regra(B2[0], B2[1], B2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B3':
				prod = prod * sigma_meet.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
		
		if ativadas[i][7] == 'S3':
			num = prod * 0
		elif ativadas[i][7] == 'S2':
			num = prod * 0.5
		elif ativadas[i][7] == 'S1':
			num = prod * 0.7
		elif ativadas[i][7] == 'CE':
			num = prod * 0.9
		elif ativadas[i][7] == 'B1':
			num = prod * 1.1
		elif ativadas[i][7] == 'B2':
			num = prod * 1.3
		elif ativadas[i][7] == 'B3':
			num = prod * 1.5

		numerador.append(num)
		denominador.append(prod)

	#x = sum(numerador)/sum(denominador)
	x4.append(sum(numerador)/sum(denominador))

#######################################################################################################

#begining Wang-Mendel Algorithm to extract a Fuzzy Rule Base (subsethood)
baseDeRegras = []		#Rule format: [ant1, ant2, ant3, ant4, ant5, ant6, ant7, cons, degree]
						#where ant = antecedent, cons = consequente, degree = product of firing degrees

baseDeRegrasFinal = []

for i in range(0,694,1):	
	novaRegra = []
	degree = 1
	for j in range(0,8):	#7 ant -> 1 cons		
		grau = subsethood.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)
		ant = 'S3'

		novo_grau = subsethood.ativa_regra(S2[0], S2[1], S2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S2'
			grau = novo_grau

		novo_grau = subsethood.ativa_regra(S1[0], S1[1], S1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'S1'
			grau = novo_grau

		novo_grau = subsethood.ativa_regra(CE[0], CE[1], CE[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'CE'
			grau = novo_grau

		novo_grau = subsethood.ativa_regra(B1[0], B1[1], B1[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B1'
			grau = novo_grau

		novo_grau = subsethood.ativa_regra(B2[0], B2[1], B2[2], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B2'
			grau = novo_grau

		novo_grau = subsethood.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+j] - 0.1, x1[i+j], x1[i+j] + 0.1)		
		if novo_grau > grau:
			ant = 'B3'
			grau = novo_grau

		degree = degree*grau
		novaRegra.append(ant)

	novaRegra.append(degree)

	for n, regra in enumerate(baseDeRegrasFinal):
		if (regra[0]==novaRegra[0]) and (regra[1]==novaRegra[1]) and (regra[2]==novaRegra[2]) and \
			(regra[3]==novaRegra[3]) and (regra[4]==novaRegra[4]) and (regra[5]==novaRegra[5]) and \
			(regra[6]==novaRegra[6]):			
			if regra[8] > novaRegra[8]:				
				continue				
			else:										
				baseDeRegrasFinal.remove(regra)		

	baseDeRegras.append(novaRegra)
	baseDeRegrasFinal.append(novaRegra)

	if i == 0:		
		baseDeRegrasFinal.append(novaRegra)	

print "tamanho da base de regras original (subsethood): "+str(len(baseDeRegras))
print "tamanho da base de regras reduzida (subsethood): "+str(len(baseDeRegrasFinal))

#Prediction of new inputs (subsethood)
x5 = []
for k in range(694,994):

	#Determine which rules will be activated for a new input
	ativadas = []

	antecedents = []
	for i in range(0,7):	#determine the antecedents
		antecedent = []
		grau = subsethood.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S3')

		grau = subsethood.ativa_regra(S2[0], S2[1], S2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S2')			

		grau = subsethood.ativa_regra(S1[0], S1[1], S1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('S1')			

		grau = subsethood.ativa_regra(CE[0], CE[1], CE[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('CE')		

		grau = subsethood.ativa_regra(B1[0], B1[1], B1[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B1')

		grau = subsethood.ativa_regra(B2[0], B2[1], B2[2], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B2')

		grau = subsethood.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[i+k] - 0.1, x1[i+k], x1[i+k] + 0.1)
		if grau > 0:
			antecedent.append('B3')

		antecedents.append(antecedent)

	#print antecedents
	combinations = list(itertools.product(*antecedents))

	for i in range(0, len(combinations)):
		for j in range(0, len(baseDeRegrasFinal)):
			if (combinations[i][0]==baseDeRegrasFinal[j][0]) and (combinations[i][1]==baseDeRegrasFinal[j][1]) and (combinations[i][2]==baseDeRegrasFinal[j][2]) and \
				(combinations[i][3]==baseDeRegrasFinal[j][3]) and (combinations[i][4]==baseDeRegrasFinal[j][4]) and (combinations[i][5]==baseDeRegrasFinal[j][5]) and \
				(combinations[i][6]==baseDeRegrasFinal[j][6]):	
				ativadas.append(baseDeRegrasFinal[j])

	#print "quantas ativadas? "+str(len(ativadas))
	#print ativadas
	numerador = []
	denominador = []
	for i in range(0, len(ativadas)):
		prod = 1
		for j in range(0,7):		
			if ativadas[i][j] == 'S3':
				prod = prod * subsethood.ativa_regra_trap(S3[0], S3[1], S3[2], S3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S2':
				prod = prod * subsethood.ativa_regra(S2[0], S2[1], S2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'S1':
				prod = prod * subsethood.ativa_regra(S1[0], S1[1], S1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'CE':
				prod = prod * subsethood.ativa_regra(CE[0], CE[1], CE[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B1':
				prod = prod * subsethood.ativa_regra(B1[0], B1[1], B1[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B2':
				prod = prod * subsethood.ativa_regra(B2[0], B2[1], B2[2], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
			elif ativadas[i][j] == 'B3':
				prod = prod * subsethood.ativa_regra_trap(B3[0], B3[1], B3[2], B3[3], x1[j+k] - 0.1, x1[j+k], x1[j+k] + 0.1)
		
		if ativadas[i][7] == 'S3':
			num = prod * 0
		elif ativadas[i][7] == 'S2':
			num = prod * 0.5
		elif ativadas[i][7] == 'S1':
			num = prod * 0.7
		elif ativadas[i][7] == 'CE':
			num = prod * 0.9
		elif ativadas[i][7] == 'B1':
			num = prod * 1.1
		elif ativadas[i][7] == 'B2':
			num = prod * 1.3
		elif ativadas[i][7] == 'B3':
			num = prod * 1.5

		numerador.append(num)
		denominador.append(prod)

	#x = sum(numerador)/sum(denominador)
	x5.append(sum(numerador)/sum(denominador))

x2 = x1[700:]

mse_mamdani = 0
mse_similarity = 0
mse_sigma_meet = 0
mse_subsethood = 0

for i in range(0,300,1):
	mse_mamdani = mse_mamdani + pow((x2[i]-x[i]),2)
	mse_similarity = mse_similarity + pow((x2[i]-x3[i]),2)
	mse_sigma_meet = mse_sigma_meet + pow((x2[i]-x4[i]),2)
	mse_subsethood = mse_subsethood + pow((x2[i]-x5[i]),2)

mse_mamdani = mse_mamdani / 300
mse_similarity = mse_similarity / 300
mse_sigma_meet = mse_sigma_meet / 300
mse_subsethood = mse_subsethood / 300

print "MSE mamdani: "+str(mse_mamdani)
print "MSE similarity: "+str(mse_similarity)
print "MSE sigma-meet: "+str(mse_sigma_meet)
print "MSE subsethood: "+str(mse_subsethood)

#pl.plot(x1, x2)
# pl.plot(range(700,1000,1),x2,'b',range(700,1000,1),x,'r--',range(700,1000,1),x3,'g--',range(700,1000,1),x4,'y--',range(700,1000,1),x5,'m--')
pl.plot(x2,'b', label='original')
pl.plot(x,'r--', label='mamdani')
pl.plot(x3, 'g--', label='similaridade')
pl.plot(x4, 'y--', label='sigma-meet')
pl.plot(x5, 'm--', label='subsethood')
pl.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=5, mode="expand", borderaxespad=0.)
pl.xlabel('$t$')
pl.ylabel('$x(t - 30)$')
#pl.show()