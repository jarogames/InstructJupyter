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
pool = Pool()

def host(id):
    import socket
    import time
    from math import sin
    #print( id )
    #time.sleep(1.0)
    sum=0
    for i in range(1,1000):
        for j in range(1,10000):
            sum=sum+sin(i/j)
    return "Rank: %d -- %s. %f" % (id, socket.gethostname(),sum+id)
####    return "Rank: %d -- %s. %f" % (id, socket.getnameinfo(),sum+id)



pool.ncpus = 4
print("Evaluate on "+str(pool.ncpus)+" cpus")
pool.servers = ('localhost:5653','localhost:5654', 'Filip:5653')


##     >>> # do an asynchronous map, then get the results
print("non blocking with wait")
res5 = pool.amap( host, range(8) )
while not res5.ready():
         time.sleep(1)
         print(stats()  )

print( "=========")
print(  "\n".join(res5.get()) )
pool.close()
pool.join()


# print("blocking uimap join")
# res5 = pool.uimap( host, range(2) ) # blocking
# print(pool)
# print(stats())
# print('\n'.join(res5))  # blocks here
# print(stats())
# print('')

# print("PIPE")
# # do one item at a time, using an asynchronous pipe
# res=[]
# for i in range(8):
#     res.append(   pool.apipe( host, i) )
# print("blocking  get() comes with apipe")
# for i in range(8):
#     print(i,'.',res[i].get() )
