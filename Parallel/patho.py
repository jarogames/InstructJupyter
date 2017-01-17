#! /usr/bin/env python3

import pathos.multiprocessing as mp
import os
import random
import time

class Pool_set:
    def pool_fun(directory_name):
         cwd=os.getcwd()
#        os.mkdir(str(directory_name))
         directory=os.path.join(cwd,str(directory_name))
#        os.chdir(directory)
#        os.system('{}'.format('sleep '+str(directory_name)))
#        cwd2=os.getcwd()
#        print(cwd2)
#        test_file = open('test_file.out','w')
#        test_file.write(cwd2)
         print("Finished in "+directory)
         time.sleep(1)
#        os.chdir(cwd)

if __name__ == '__main__':


    config=[]
    pool_set = Pool_set
    for i in (random.sample(range(1,100),4*4)):
        config.append(i)

    pool_size = mp.cpu_count()
    pool = mp.Pool(processes=pool_size,maxtasksperchild=1,)

    pool_outputs = pool.map(pool_set.pool_fun,config)
    pool.close()
    pool.join()
    
