#!/usr/bin/env python3
import os
import time
import signal
import sys
def signal_handler(signal, frame):
        print('I got signal (10/12)', signal)
        # NO GETPID HERE!
#        print('I ',os.getpid(),'got signal', signal)
        sys.exit(0)

children=[]
signal.signal(signal.SIGUSR1, signal_handler)        
signal.signal(signal.SIGUSR2, signal_handler)        
for i in range(2):
    print( '**********%d***********' % i )
    pid = os.fork()
    if pid == 0:
        print( "%d just was created." % os.getpid() )
        for i in range(5):
            time.sleep(1)
        print( '    child ',os.getpid(),'quit')
        quit()
    else:
        print( "%d has  created %d." % (os.getpid(), pid) )
        children.append(pid)

############## main parent
for pid in children:
    time.sleep(0.1)
    print('child=',pid,'sending')
    os.kill( pid , signal.SIGUSR1)
############## exit
for pid in children:
    print('waiting for',pid)
    os.waitpid(pid, 0)
