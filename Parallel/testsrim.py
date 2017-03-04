#!/usr/bin/env python3
import NuPhyPy.srim.srim as srim
import pandas as pd
import NuPhyPy.db.ReadNubase as db


from pathos.parallel import stats
from pathos.parallel import ParallelPool as Pool
import time

pool = Pool()

def host(id ,TRIMIN1):
    import socket
    import os
    import NuPhyPy.srim.srim as srim
    #print('starting TRIM with ',id,ipath)
    tmpp=srim.run_srim(ipath,TRIMIN1, silent=True)  
    #print('done TRIM')
    return ( id,socket.gethostname(),tmpp )
    #return tmpp

alpha=db.isotope(4,2)
h1=db.isotope(1,1)
he3=db.isotope(3,2)
c12=db.isotope(12,6)
c13=db.isotope(13,6)
c14=db.isotope(14,6)
n14=db.isotope(14,7)
o16=db.isotope(16,8)

Eini=5.800
rho=2.253
mgcm2=srim.get_mgcm2( 25.5,  rho )
print( mgcm2,  srim.get_um( mgcm2, rho))
ipath=srim.CheckSrimFiles()
TRIMIN=srim.PrepSrimFile( ion=h1, energy=Eini, angle=0., number=100 ,
    mater='c', thick=mgcm2, dens=rho  )
#tmpp=srim.run_srim(ipath, TRIMIN)
#exit()

pool.ncpus =1
pool.servers = ('localhost:5653','localhost:5654', 'Filip:5653')
#pool.servers = ('localhost:5653','localhost:5654', 'Filip:5653','aaron:5653')
totalchunks=3
params=[ TRIMIN, TRIMIN, TRIMIN]
res5 = pool.amap( host, range(totalchunks) , params )
while not res5.ready():
         time.sleep(1)
         print( stats()  )
for f in res5.get():
    print( f[0],'===',f[1],'=======================')
    print( f[2]['e'])
pool.close()
pool.join()
