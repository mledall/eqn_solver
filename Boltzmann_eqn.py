# General Packages
import numpy as np
from IPython.display import Image # allows to display saved images inline
import scipy.integrate as spint
import scipy.special as spsp
import scipy.stats as spstat
import matplotlib.pyplot as plt
import time as time
# Random package
import random as random

zmin=0.01
zmax=100
dz=0.0001
z=np.arange(zmin,zmax,dz)
nz=len(z)

Yleq=3.0*4**(-1)
Y0 = 0
Yl0 = 1e-20
state0=[Y0,Yl0]

def meta_parameters():
	print (' zmin = %f,\n zmax = %f,\n dz = %f,\n Yleq = %f,\n Y0 = %f,\n Yl0 = %f,\n ' %(zmin, zmax, dz, Yleq, Y0, Yl0))

def Yeq(z):
    fun=(3.0/8)*z**2*spsp.kn(2,z)
    return(fun)

def D(z,K):
    fun=K*z**2*(spsp.kn(1,z)/spsp.kn(2,z))*Yeq(z)
    return(fun)

def Boltzmann_sol(eps, K):
	def Boltzmann_eqn(state, z): # This function sets calculates the derivatives to be used in odeint solver.
	    y1=state[0]
	    yl=state[1] 
	    Y1d=D(z,K)*(1-y1*Yeq(z)**(-1))*z**(-1)
	    Yld=(eps*(y1/Yeq(z)-1)-yl/(2*Yleq))*D(z,K)/z
	    return(Y1d, Yld)

	abserr = 1.0e-13
	relerr = 1.0e-13
	sol=spint.odeint(Boltzmann_eqn,state0,z, atol=abserr, rtol=relerr,hmax=0.0,hmin=0.0)  

	Y1,Yl=sol.T
	Ylf = Yl[nz-1]
	return (Y1, Yl, Ylf)


def final_asymm(eps,K):
    Ylf = Boltzmann_sol(eps, K)[2]
    return(Ylf)

def efficiency(eps):
    K = np.arange(0, 10, .1)
    kappa_tab = []
    for i in xrange(len(K)):
        k = K[i]
        kappa = final_asymm(eps,k)*eps**(-1)
        kappa_tab.append(kappa)
    return kappa_tab

