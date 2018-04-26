import numpy as np
import pandas as pd
import time as time

from Boltzmann_eqn import *

def data_gen():
	epsmin, epsmax, deps = 1e-9, 1e-7, 1e-9
	Kmin, Kmax, dK = 0, 10, 0.01
	eps = np.arange(epsmin, epsmax, deps)
	K = np.arange(Kmin, Kmax, dK)
	N = len(eps) * len(K)
	n = 0
	v = []
	t0 = time.time()
	print '- Starting the calculation'
	for i in range(len(eps)):
		for j in range(len(K)):
			n = n+1
			Ylf = final_asymm(eps[i],K[j])
			if 1.2e-9 > Ylf > 1e-9:
				v.append([eps[i],K[j],Ylf, 'good'])
			else:
				v.append([eps[i],K[j],Ylf, 'not good'])
			if ( (n+1) % 100 == 0 ):
				print(' -- Calculated %d points out of %d' % (n,N))
	asymm = np.array(v)
	tf = time.time()-t0
	print('- Finished calculating in %f' %tf)
	eps = asymm[:,0]
	K = asymm[:,1]
	Ylf = asymm[:,2]
	result = asymm[:,3]

	dfeps = pd.DataFrame(data = eps, columns = ['eps']) #index = ['a','b','c']
	dfK = pd.DataFrame(data = K, columns = ['K'])
	dfYlf = pd.DataFrame(data = Ylf, columns = ['Ylf'])
	dresult = pd.DataFrame(data = result, columns = ['result'])
	data =  pd.concat([dfeps, dfK, dfYlf, dresult], axis = 1)
	print '- Writing to Asymm_data.csv'
	data.to_csv('Asymm_data.csv', sep = ',')
	print '- Finished writing'

data_gen()

