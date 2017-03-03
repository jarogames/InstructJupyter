#!/usr/bin/env python3
#
from pathos.parallel import stats
from pathos.parallel import ParallelPool as Pool
import time

pool = Pool()

def host(id ):
    import socket
    #print("kunik co je")
    #return str(id)
    time.sleep(1)
    result=id+5
    return "{},{},{}".format(id,socket.gethostname(),result)
pool.ncpus = 1  # when nodes replaced by 1
pool.servers = ('localhost:5653','localhost:5654')
totalchunks=5
res5 = pool.amap( host, range(totalchunks)  )
while not res5.ready():
         time.sleep(1)
         print(stats()  )
print( '##'.join(res5.get())  )
pool.close()
pool.join()
print( "=========Printout:")
aaa='_'.join(res5.get())
csvheader="chunk,host,result\n"
csv=csvheader+"\n".join(res5.get()) 
print( '\n==REAL PRINT==\n',csv)
