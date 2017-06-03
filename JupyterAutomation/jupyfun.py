#!/usr/bin/python3
"""
This is a way to generate jupyter notebook
and
HTML afterwards
I dont see a way to append to a jupyter notebook.....

./jupyfun.py  ... from some directory to parse a subdirectory

 *  -o outputname ... .ipynb  will be appended
 *  -d run011 ...  this script is run from directory, that contains subdirectory /run11/ with data
 * -html ...  create also html file - not useful in a real jupyter
"""
import nbformat as nbf
import glob
import argparse
import os

parser=argparse.ArgumentParser(description="""
 ... 
""")

parser.add_argument('-o','--output',  default="", help='', required=True)

parser.add_argument('-d','--diveinto', default="", help='')
#parser.add_argument('-t','--time',  default=9, type=int, help='seconds between questions')
#parser.add_argument('-p','--path_to_save',  default="./", help='')
parser.add_argument('-html','--html', action="store_true", help='')

args=parser.parse_args()


if args.diveinto[-1]!='/': args.diveinto=args.diveinto+'/'

print('I am in directory ........ ',os.getcwd())
###if len(args.diveinto)>0 : os.chdir( args.diveinto )

nb = nbf.v4.new_notebook()
basename=os.path.split(os.getcwd())[1]

text = "# "+basename+'  \n # '+args.diveinto +"\n"
text=text+" auto-generated notebook.\n\n"
text=text+" Contains jpgs from the directory **"+os.getcwd()+'/'+args.diveinto+"**\n\n"

COLUMNS=2
WIDTH=450


lines=[]
topline=["| "]*(COLUMNS+1)
midline=["|-"]*(COLUMNS) 
#print( "".join(topline) )
#print( "".join(midline) )

photos=" ".join(topline) + '\n' + " ".join(midline) + ' |\n'
i=1
print('========== globing===',args.diveinto+"*.jpg")
for jpg in glob.glob(args.diveinto+"*.jpg"):
    print('i... ',i,'.  JPG FILE')
    line='<a href="'+jpg+'"><img src="'+jpg+'" width="'+str(WIDTH)+'"></img></a>'
    #
    # line='<img src="'+jpg+'" width="'+str(450)+'"></img>'
    lines.append( line )
    if i%COLUMNS==0:
        print('i... preparing line')
        photos=photos+"| "+"|".join(lines)+'|\n'
        lines=[]
    i=i+1

if len(lines)!=0:
    print('i... preparing last incomplete line')
    photos=photos+"| "+"|".join(lines)+'|\n'
    
#print(photos)

##############################################
lines=[]
topline=["| "]*(COLUMNS+1)
midline=["|-"]*(COLUMNS) 

zips=" ".join(topline) + '\n' + " ".join(midline) + ' |\n'
i=1
for jpg in glob.glob(args.diveinto+"*.zip"):
    print('i... ',i,'.  ZIP FILE')
    line='<a href="'+jpg+'">'+jpg+'</a>'
    #
    # line='<img src="'+jpg+'" width="'+str(450)+'"></img>'
    lines.append( line )
    if i%COLUMNS==0:
        print('i... preparing line')
        zips=zips+"| "+"|".join(lines)+'|\n'
        lines=[]
    i=i+1

if len(lines)!=0:
    print('i... preparing last incomplete line')
    zips=zips+"| "+"|".join(lines)+'|\n'
    
print(zips)


#photos="""\
#| | | |
#|-|-|-|
#|1 |2 |3 |
#"""

code = """\
%pylab inline
hist(normal(size=2000), bins=50);"""

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_markdown_cell('## JPG FILES:\n\n'+photos),
               nbf.v4.new_markdown_cell('## ZIP FILES:\n\n'+zips) ]
#               nbf.v4.new_code_cell(code) ]

#################################################
################# OUTPUT SECTION ################
fname = 'test.ipynb'
fname=args.output+'.ipynb'

##if len(args.diveinto)>0 : os.chdir( '..' )


with open(fname, 'w') as f:
    nbf.write(nb, f)
    
import subprocess
print('compile with jupyter')
CMD="jupyter nbconvert --execute --inplace "+fname
p=subprocess.check_call( CMD , shell=True)

if args.html:
    print('translate to html')
    CMD='jupyter nbconvert --to html '+fname
    p=subprocess.Popen( CMD , shell=True)
