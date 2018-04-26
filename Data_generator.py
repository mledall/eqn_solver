import numpy as np
import pandas as pd

from Boltzmann_eqn import *

def data_gen():
	eps = np.arange(1e-8, 1e-7, 1e-8)
	K = np.arange(0, 10, 0.1)
	v = []
	for i in range(len(eps)):
		for j in range(len(K)):
			Ylf = final_asymm(eps[i],K[j])
			if 1.2e-9 > Ylf > 1e-9:
				v.append([eps[i],K[j],Ylf, 'good'])
			else:
				v.append([eps[i],K[j],Ylf, 'not good'])
	asymm = np.array(v)
	eps = asymm[:,0]
	K = asymm[:,1]
	Ylf = asymm[:,2]
	result = asymm[:,3]

	dfeps = pd.DataFrame(data = eps, columns = ['eps']) #index = ['a','b','c']
	dfK = pd.DataFrame(data = K, columns = ['K'])
	dfYlf = pd.DataFrame(data = Ylf, columns = ['Ylf'])
	dresult = pd.DataFrame(data = result, columns = ['result'])
	data =  pd.concat([dfeps, dfK, dfYlf, dresult], axis = 1)

	data.to_csv('test.csv', sep = ',')

data_gen()

