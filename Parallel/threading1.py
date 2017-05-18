#!/usr/bin/python3

import threading
import time
import subprocess
import sys  # write to std output

def worker():
    """thread worker function"""
    print( threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    #print( threading.currentThread().getName(), 'Exiting')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    time.sleep(0.2)
    t.start()
print('now i am free to end')


toolbar_width = 40
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start after '['

for i in range(15):
    if not threads[-1].isAlive(): break
    time.sleep(1)
    destin='$HOME/typescript23'
    output = subprocess.check_output('wc -l '+destin+' | cut -d " " -f 1', shell=True).decode('utf8').rstrip()
    output=int(output)

    nmax=2000
    ratio=i*300/nmax
    if ratio>1.0:ratio=1.0
    toolfull=int(toolbar_width*ratio)
    bar1="[%s" % ("#" * toolfull   )
    bar2="%s]%d/%d" % (" " * (toolbar_width-toolfull+0), output,nmax  )
    bar=bar1+bar2
    sys.stdout.write("\b" * (len(bar)+1)) # return to start a    
    sys.stdout.write(bar)
    sys.stdout.flush()
