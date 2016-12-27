#!/home/mraz/anaconda3/bin/python3
from os.path import expanduser   #home dir
import mysql.connector
home = expanduser("~")
dbase='test'
with open(home+'/.'+dbase+'.mysql', 'r') as content:
    allf = content.read().split('\n')
config = {
  'user': allf[1],  'password': allf[2],  'host': allf[0],
  'database': dbase,  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query = ("SELECT * FROM db ORDER BY day LIMIT 30")
#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)
cursor.execute(query)
#print( cursor.column_names ) 
dayw=['mon','tue','wed','thu','fri','sat','SUN']
#for i in range(len(cursor)):
#    cursor[i,1]=dayw[cursor[i,1]]
#    #print( i[0], dayw[i[1]] ,i[2:] )
#cnx.close()
#import pandas as pd
df=pd.DataFrame(  [i for i in cursor] , columns=cursor.column_names )
#df['dow']=df['dow'].map({1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat',0:'SUN'})
#df[['day','dow','pruser','manzetka']]
print(df)
