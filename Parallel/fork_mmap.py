#!/usr/bin/env python3
import os
import time
import signal
import sys
############### for mmap:
import mmap
import contextlib



###########################
#  to exit all, one needs a signal
##########################
def signal_handler(signal, frame):
    print('S___  I got signal (10 or 12)', signal)
    # NO GETPID HERE!
    #print('I ',os.getpid(),'got signal', signal)
    sys.exit(0)


def child_code_0():
    for i in range(5):
        time.sleep(1)
        m.seek(0)
        print( str(i)+'___ ',m.read().decode('utf8'))
def child_code_1():
    for i in range(5):
        time.sleep(1.02)
        m.seek(0)
        print( str(i)+'___ ',m.read())
#



########################################
#  start
# 
########################################
MMFILE="mmap.txt"
children=[]
signal.signal(signal.SIGUSR1, signal_handler)
signal.signal(signal.SIGUSR2, signal_handler)
with open(MMFILE, "wb") as f:
    f.write(b"12345678901234567890\n")
f=open('mmap.txt', 'rb+')
m=mmap.mmap(f.fileno(), 0)
time.sleep(1)
m.seek(0) # rewind
m.write(b"AHOJ ")
m.flush()
time.sleep(1)
m.seek(0) # rewind
m.write(b"NAZDAR ")
m.flush()
        
for i in range(2):
    pid = os.fork()
    if pid == 0:
    #################################################
    #           CHILD CODE HERE
    #################################################
        print( "c___ %d i am child #%d" % (os.getpid(), i ) )
        if i==0: child_code_0()
        if i==1: child_code_1()
        print( '!___    child ',os.getpid(),'quit')
        quit()
    #################################################
    #           CHILD CODE ENDS HERE
    #################################################
    else:
        children.append(pid)  # FILL THE LIST OF CHILDERN



        
################################## main parent
m.seek(0) # rewind
m.write(b"kuku ")
m.flush()

time.sleep(1)
m.seek(0) # rewind
m.write(b"KUKU ")
m.flush()
time.sleep(1)

for pid in children:
    time.sleep(0.1)
    print('k... sending kill to child=',pid,'')
    os.kill( pid , signal.SIGUSR1)
################################## exit
for pid in children:
    print('i... waiting for',pid)
    os.waitpid(pid, 0)
    
    
