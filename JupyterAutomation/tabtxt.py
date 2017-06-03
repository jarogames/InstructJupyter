#!/usr/bin/python3

import glob
import sys
from IPython.display import display, Markdown, Latex

if len(sys.argv)==1:
    DATA=""
else:
    DATA=sys.argv[1]+'/'


g=sorted(glob.glob(DATA+"*.jpg"))
g=[ '<img src="'+x+'"></img>'   for  x  in g ]
h=[ "<td><a href=\"{}\">{}</a></td>".format(x,x) for x in g]
h=list('<table><tr>'+l  if n%4==0 else l for n, l in enumerate(h)  )  
h=list(l+'</tr></table>\n'  if n%4==3 else l for n, l in enumerate(h)  )  
print("\n".join(h))


g=sorted(glob.glob(DATA+"*.zip"))
h=[ "<td><a href=\"{}\">{}</a></td>".format(x,x) for x in g]
h=list('<table><tr>'+l  if n%4==0 else l for n, l in enumerate(h)  )  
h=list(l+'</tr></table>\n'  if n%4==3 else l for n, l in enumerate(h)  )  
print("\n".join(h))

g=sorted(glob.glob(DATA+"*.txt"))
h=[ "<td><a href=\"{}\">{}</a></td>".format(x,x) for x in g]
h=list('<table><tr>'+l  if n%4==0 else l for n, l in enumerate(h)  )  
h=list(l+'</tr></table>\n'  if n%4==3 else l for n, l in enumerate(h)  )  
print("\n".join(h))


g=sorted(glob.glob(DATA+"*.asc"))
h=[ "<td><a href=\"{}\">{}</a></td>".format(x,x) for x in g]
h=list('<table><tr>'+l  if n%4==0 else l for n, l in enumerate(h)  )  
h=list(l+'</tr></table>\n'  if n%4==3 else l for n, l in enumerate(h)  )  
print("\n".join(h))
#display(Markdown("\n".join(h) ) )

