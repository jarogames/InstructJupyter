#!/usr/bin/env python3
#
# nodes=(localhost)
# for i in "$nodes[@]"; do ssh -f $i /home/username/bin/ppserver.py -p $portnum -w 2 -t 30 &done
#
#https://github.com/uqfoundation/pathos/blob/master/pathos/multiprocessing.py
#
# too diffic
#http://nullege.com/codes/show/src@p@a@pathos-HEAD@tests@test_mp.py/26/pathos.multiprocessing.ProcessingPool.amap
#
#
#
from pathos.parallel import stats
from pathos.parallel import ParallelPool as Pool
import time
from decimal import Decimal, getcontext   # PI calc

pool = Pool()


def calculpi():
    from decimal import Decimal, getcontext   # PI calc
    #print( 'print pii ....' )
    getcontext().prec=3500
    pii=sum(1/Decimal(16)**k * 
            (Decimal(4)/(8*k+1) - 
             Decimal(2)/(8*k+4) - 
             Decimal(1)/(8*k+5) -
             Decimal(1)/(8*k+6)) for k in range(3500))
   # print( 'print pii',pii )
    return pii

def host(id):

    import socket
#    import time
    from math import sin
    #print( id )
    #time.sleep(1.0)
    sum=0
#    for i in range(1,1000):
#        for j in range(1,10000):
#            sum=sum+sin(i/j)
    result="Rank: %d -- %s. %f" % (id, socket.gethostname(),sum+id)
    result=str( calculpi() )
    return "{},{},{}".format(id,socket.gethostname(),result)
####    return "Rank: %d -- %s. %f" % (id, socket.getnameinfo(),sum+id)



pool.ncpus = '*'
pool.ncpus = 'autodetect'
pool.ncpus = 0  # when nodes replaced by 1
#pool.nodes='*'
print("Evaluate on "+str(pool.ncpus)+" cpus")
pool.servers = ('localhost:5653','localhost:5654', 'Filip:5653','aaron:5653')


##     >>> # do an asynchronous map, then get the results
totalchunks=16
print("non blocking with wait", )
res5 = pool.amap( host, range(totalchunks) )
while not res5.ready():
         time.sleep(1)
         print(stats()  )

print( "=========")
csvheader="chunk,host,result\n"
csv=csvheader+"\n".join(res5.get()) 
####print( csv,' === CSV' )
pool.close()
pool.join()
######### get csv to pandas
from io import StringIO
TESTDATA=StringIO(csv)
import pandas as pd
df=pd.read_csv( TESTDATA ,sep=',')

import prettytable    
output = StringIO()
df.to_csv(output)
output.seek(0)
pt = prettytable.from_csv(output)
#print('pretty table:\n',pt)
print( 'pandas:\n',df )
