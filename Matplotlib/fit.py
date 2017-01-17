#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.arange(0.1, 4, 0.5)
y = 1/np.exp(-x)
yerr = 0.01 + 1.2*np.sqrt(x)
xerr = 0.1 

plt.figure()
plt.errorbar(x, y, fmt="s", xerr=xerr, yerr=yerr)   #plt.plot(x, y, "bo-" )
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")

from scipy import optimize

fitfunc = lambda p, x: p[0]*x*x*x+p[1]*x*x+p[2]*x # Target function
errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
def residuals(p,x,y):
    return abs(y-fitfunc(p,x))
p0 = [1.3, -3.6, 5.2 ] # Initial guess for the parameters
p1,pcov,infodict,errmsg,success=optimize.leastsq(errfunc,p0[:],args=(x, y),full_output=1,epsfcn=0.0001  )
#?p1,pcov,info,msg,ler=optimize.leastsq(residuals,p0,args=(x, y) , full_output=True )
#p1,sim=optimize.leastsq(residuals,p0,args=(x, y)  )
#NONO p1,pcov=optimize.curve_fit(errfunc, x, y, p0, sigma=yerr, epsfcn=0.0001 )
print(p1)
time = np.linspace(x.min(), x.max(), 100)
plt.plot( time, fitfunc(p1, time) ,"r-" ) # Plot of the data and the fit
plt.errorbar(x, y, fmt="b ", xerr=xerr, yerr=yerr)   #plt.plot(x, y, "bo-" )
