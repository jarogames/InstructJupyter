#!/home/mraz/anaconda3/bin/python3
#########################
#
#  i just read from mysql
#  transform, filter
#  and plot data 
#
##########################
from os.path import expanduser   #home dir
import datetime
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
def unglitch(li):
	for i in range( len(li)-2):
		#print(i)
		delta=abs(li[i]-li[i+2])
		if  abs(li[i]-li[i+1])>3*delta and abs(li[i+1]-li[i+2])>3*delta:
			li[i+1]=(li[i]+li[i+2])/2
	#li=li
	return li


today = datetime.datetime.now()
one_day = datetime.timedelta(hours=24)
print( 'One day  :', one_day)

week = today - one_day
print( today )
print( week )
print('ctime:', today.ctime() )

home = expanduser("~")
##########################
#
#  MYSQL
#
##########################
dbase='test'  ## TEST dbase feat
table='db'
with open(home+'/.'+table+'.mysql', 'r') as content:
    allf = content.read().split('\n')
print(allf[0])
config = {
  'user': allf[1],  'password': allf[2],  'host': allf[0],
  'database': dbase,  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query =("SELECT * FROM "+table+" WHERE t > '"+str(week)+"' ORDER BY t DESC")
print(query)
cursor.execute(query)
listx=np.array( list([i for i in cursor]) )
#listx[:,1]=unglitch(listx[:,1])  # red T
#listx[:,2]=unglitch(listx[:,2])  #  red H
#listx[:,3]=unglitch(listx[:,3])   # black T
#listx[:,4]=unglitch(listx[:,4])   # black H
listx[:,5]=unglitch(  list(listx[:,5]) )   # cyan T   glitchin
listx[:,6]=unglitch( list(listx[:,6]) )   # cyan H
#######################
#print( 'test', np.log( list(listx[:,6]) ) )
DEWP56=243.04*(np.log( list(listx[:,6]/100.0) )+((17.625*listx[:,5])/(243.04+listx[:,5])))/(17.625-np.log( list(listx[:,6]/100.0))-((17.625*listx[:,5])/(243.04+listx[:,5])))
DEWP12=243.04*(np.log( list(listx[:,2]/100.0) )+((17.625*listx[:,1])/(243.04+listx[:,1])))/(17.625-np.log( list(listx[:,2]/100.0))-((17.625*listx[:,1])/(243.04+listx[:,1])))
DEWP34=243.04*(np.log( list(listx[:,4]/100.0) )+((17.625*listx[:,3])/(243.04+listx[:,3])))/(17.625-np.log( list(listx[:,4]/100.0))-((17.625*listx[:,3])/(243.04+listx[:,3])))
df=pd.DataFrame( listx  , columns=cursor.column_names )
#print(df)
#######################################################END OF MYSQL 1
#week=today -  datetime.timedelta(hours=168)



table='rain3'
with open(home+'/.'+table+'.mysql', 'r') as content:
    allf = content.read().split('\n')
print(allf[0])
config = {
  'user': allf[1],  'password': allf[2],  'host': allf[0],
  'database': dbase,  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query =("SELECT * FROM "+table+" WHERE t > '"+str(week)+"' ORDER BY t DESC")
print(query)
cursor.execute(query)
listy=np.array( list([i for i in cursor]) )
dfr=pd.DataFrame( listy, columns=cursor.column_names )
print(dfr)


from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
from matplotlib.dates import MONDAY
# every 3rd month
#mondays = WeekdayLocator(MONDAY)
#months = MonthLocator(range(1, 13), bymonthday=1, interval=3)
#fig = plt.figure(figsize=(4, 3), dpi=100 )
########################
#
#
#
###########################
monthsFmt = DateFormatter("%H:%M(%d)")
fig, ax = plt.subplots( figsize=(6, 5), dpi=100 )
#ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
#ax.xaxis.set_minor_locator(mondays)
#ax.autoscale_view()
#ax.grid(True)
#fig.autofmt_xdate()
plt.plot( df.t, df.a ,'r.-')
plt.plot( df.t, DEWP12 ,'r--', linewidth=2)
#plt.plot( df.t, df.b ,'r.-')
plt.plot( df.t, df.c ,'k.-')
plt.plot( df.t, DEWP34 ,'k--', linewidth=2)
#plt.plot( df.t, df.d ,'k.-')
plt.plot( df.t, df.e ,'c.-')
plt.plot( df.t, DEWP56 ,'c--', linewidth=2)
#plt.plot( df.t, df.f ,'c.-')
plt.plot( df.t, df.g ,'m.-')
plt.plot( df.t, df.h ,'g.-')
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.savefig('/tmp/dewpoint.jpg', bbox_inches='tight')


fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
#ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
#ax.xaxis.set_minor_locator(mondays)
#ax.autoscale_view()
#ax.grid(True)
#fig.autofmt_xdate()
#plt.plot( df.t, df.a ,'r.-')
#plt.plot( df.t, df.b ,'r.-')  #HUMI
plt.plot( df.t, df.c ,'k.-')
#plt.plot( df.t, df.d ,'k.-')   #HUMI
plt.plot( df.t, df.e ,'c.-')
#plt.plot( df.t, df.f ,'c.-')     #HUMI
plt.plot( df.t, df.g ,'m.-')
#plt.plot( df.t, df.h ,'g.-')
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.savefig('/tmp/tempin.jpg', bbox_inches='tight')

#####################################
#
#    DEW
#
#######################################
fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
#ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
#ax.xaxis.set_minor_locator(mondays)
#ax.autoscale_view()
#ax.grid(True)
#fig.autofmt_xdate()
#plt.plot( df.t, df.a ,'r.-')
plt.plot( df.t, df.b ,'r.-')
#plt.plot( df.t, df.c ,'k.-')
plt.plot( df.t, df.d ,'k.-')
#plt.plot( df.t, df.e ,'c.-')
plt.plot( df.t, df.f ,'c.-')
#plt.plot( df.t, df.g ,'m.-')
#plt.plot( df.t, df.h ,'g.-')
plt.grid(True)
plt.gcf().autofmt_xdate()
plt.savefig('/tmp/humid.jpg', bbox_inches='tight')


##############################################
#
#  RAIN
#
#
########################


fig, ax = plt.subplots(figsize=(6,5), dpi=100)
#ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
#week wid=0.01
wid=0.02
plt.bar( listy[:,0] , listy[:,2] , width=wid ,color='grey')
plt.bar( listy[:,0] , listy[:,1] , width=wid/2 , alpha=0.5 )
#plt.bar( listy[:,0]+wid , listy[:,2] , width=wid )

plt.grid(True)
#plt.yscale( 'log' , nonposy='clip')
plt.gcf().autofmt_xdate()
plt.savefig('/tmp/rain.jpg', bbox_inches='tight')

#plt.show()
#import Image
#Image.open('testplot.png').save('testplot.jpg','JPEG')
