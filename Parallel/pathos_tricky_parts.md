I like to use only servers in a list. Not local.
--------------------------------------------

I can by setting

```pool.ncpus = 0```

in case I modified the file
```
/home/ojr/anaconda3/lib/python3.5/site-packages/pathos/parallel.py
```
and removed **nodes** and put **1**
```
            chunksize, extra = divmod(length, 1 * elem_size)
#            chunksize, extra = divmod(length, nodes * elem_size)
```


Versions of libraries
----------------------
When 
```
ERROR:root:PP version mismatch (local: pp-1.6.4.7.1, remote: pp-1.6.4.6)
```
error appears, update ppft
```
pip   install --upgrade ppft
```


Run servers:
------------
```
/home/ojr/anaconda3/bin//ppserver.py -p 5653 -w 4 -t 3600
```

Carefull - once the server runs, changes in library are not known to the server!
Needs to restart.
