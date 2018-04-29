import numpy as np
import pandas as pd
import time as time

from Boltzmann_eqn import *

def data_gen():
	epsmin, epsmax, deps = 1e-9, 1e-7, 1e-9
	Kmin, Kmax, dK = 0, 50, 0.01
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
				v.append([eps[i],K[j],Ylf, 'good', 0])
			else:
				v.append([eps[i],K[j],Ylf, 'not good', 1])
			if ( (n+1) % 100 == 0 ):
				print(' -- Calculated %d points out of %d' % (n,N))
	tf = time.time()-t0
	print('- Finished calculating in %f seconds' %tf)
	data = pd.DataFrame(data = v, columns = ['eps', 'K', 'Ylf', 'result', 'binary result'])
	print '- Writing to Asymm_data.csv'
	data.to_csv('Asymm_data.csv', sep = ',')
	print '- Finished writing'


data_gen()

