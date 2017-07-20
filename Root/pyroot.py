#!/usr/bin/python3
'''
 Example how to save a histogram

 look at:
 https://www-zeuthen.desy.de/~middell/public/pyroot/pyroot.html
store parameters inside TH1:
https://root-forum.cern.ch/t/storing-info-inside-a-th1/6035
#
http://wlav.web.cern.ch/wlav/pyroot/using.html
'''

import numpy as np
CHANS=4096
ss=np.linspace(0, CHANS-1, CHANS)
ss=  1000*np.sin(3.14*ss/CHANS) 
print( ss[1] )
import ROOT
f=ROOT.TFile("n42_test.root","recreate")
h1=ROOT.TH1F("h1","Kurnik", CHANS,0, CHANS)
entries=0
for i in range(ss.shape[0]):
    entries=entries+ss[i]
    h1.SetBinContent( i, ss[i] )
h1.SetEntries( entries )
n1=ROOT.TNamed("start",   "{}".format("01-01-2017")  )
n2=ROOT.TNamed("duration","{}".format(1234) )
n3=ROOT.TNamed("DT",      "{}".format("4.5%") )
n4=ROOT.TNamed("CPS",     "{}".format( 12001.5) )
h1.GetListOfFunctions().Add(n1);
h1.GetListOfFunctions().Add(n2);
h1.GetListOfFunctions().Add(n3);
h1.GetListOfFunctions().Add(n4);

h1.Write()
f.Close()
