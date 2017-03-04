#!/usr/bin/env python
import qrcode
#import image
from  PIL import Image
import base64
###########3movie part
import numpy as np
import gizeh
import moviepy.editor as mpy


rimage=open('pudorys.jpg','rb')
imgread=rimage.read()
line=base64.encodestring(imgread)

with open('/home/ojr/09_DATA_ANALYSIS/OJRhpex/10_Fresco_ltd/02_src/fresco/man/fresco8.tex','r') as f:
    line=f.read()

print( 'total length',len(line) )

enl_size=(480,480)  # qr will be scaled up
new_size=(640,480)  # put onto canvas
n=2000   #  chunk size
chunks=[line[i:i+n] for i in range(0, len(line), n)]

####################################
i=1
allclips=[]
for chunk in chunks:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=4,
    )
    qr.add_data(chunk)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    print(i,'/',len(chunks),'qr size', img.size)
    i=i+1
    if img.size>enl_size:
        print('Cannot continue',img.size)
        quit
    img2 = img.resize( enl_size )
    new_im = Image.new("RGB", new_size, color=(222, 222, 222)) 
    new_im.paste(img2, ( int((new_size[0]-enl_size[0])/2),
                      int((new_size[1]-enl_size[1])/2)))
    new_im.save('qr.png')
    clip = mpy.ImageClip( 'qr.png',duration=0.3)
    allclips.append(clip)

##################### videopart ###############
print('write')
video=mpy.concatenate( allclips )
video.write_videofile("qr.mp4",fps=3,codec='libx264')
    
