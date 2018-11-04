

# this script works with the amazing drawbot and pagebot

# download here:
    
#     http://www.drawbot.com/
#     https://github.com/PageBot/PageBot

# I wish you good luck! If you have simple questions or get stuck
# please contact me at contact@renaudfutterer.com

# but please I dont do support I am a real beginner at this
# I just managed to make this work reading the docs and other
# scripts from the example.

# If you improve this and would like to share it, please put it back on 
# gitHub and let me know!

# peace

# Renaud

# check out my work http://www.renaudfutterer.com
# and follow me on instagram here http://www.instagram.com/renaudlondon/



# Here I import all the library needed, good luck to install them!

from __future__ import division
from random import random
from pagebot.contributions.filibuster.blurb import blurb
from pagebot.toolbox.color import Color
from pagebot.fonttoolbox.objects.family import getFamily
from pagebot.fonttoolbox.objects.font import findFont
from pagebot.style import *
from pagebot.document import Document
from pagebot.conditions import *
from pagebot.elements import *
from pagebot.contexts.platform import getContext
from pagebot.fonttoolbox.variablefontbuilder import getVarFontInstance, getConstrainedLocation
import re
   
   

# here is the main variables

font = findFont('VarsityGX') # here is the fonts
print(font.axes)
context = getContext()
title=''
content=''

# mode = 'Anim', 'Iter', 'Words' 
mode = 'Anim'
note = 'width'
ext = 'mov' #gif, mov, pdf
saver = 'on'
singleline = 'off'
fps = 25
frames = 25# 1 for still
H = 1080
W = 1440

# here are the value min/max of the iterarions

WG = [400,400,400,950]
WD = [100,75,75,200]
SL = [0,0,0,0]
CT = [0,0,0,0]

FONTSIZE = 150

line1='ABCDEF'
line2='GHIJKL'
line3='MNOPQR'
line4='STUVW'
line5='XYZ' 
line6='' 
line7=''
add = '\n'
PaddingTop = 180
PaddingLeft = 0
PaddingRight = 0
LHeight = 0.6
Justify = CENTER
if singleline == 'on':
    lines=line1
else:
    lines=line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5
TextLen = range(len(lines))

def makeIteration(startWGTH,endWGTH,startWDTH,endWDTH, startSLNT, endSLNT, startCNTR, endCNTR):
    template = Template(w=W, h=H)
    
    s = ''
    bs = context.newString(s)
    for i in TextLen:
        save()
        f = i / len(lines)
        WGTH = startWGTH + (f * (endWGTH - startWGTH))
        WDTH = startWDTH + (f * (endWDTH - startWDTH))
        SLNT = startSLNT + (f * (endSLNT - startSLNT))
        CNTR = startCNTR + (f * (endCNTR - startCNTR))
        # SLNT = round(startSLNT + (f * (endSLNT - startSLNT)))
        # wght=WGHT, wdth=WDTH, slnt=SLNT, CNTR=CNTRATTR, CNTN=CNTNATTR
        location = getConstrainedLocation(font, dict(wght=WGTH, wdth=WDTH, slnt=SLNT, CNTR=CNTR))
        instance = getVarFontInstance(font, location, normalize=True, cached=False, lazy=False)
        style = dict(font=instance.path, fontSize=FONTSIZE, rLeading=LHeight, xTextAlign=Justify, textFill=(0, 0, 0,1))
        title = context.newString(lines, style=style)
        bs.__add__(context.newString((lines[i]),style=style))
        restore()
    newTextBox(bs, parent=template, name='Other element',  pt=PaddingTop, pr=PaddingRight, pl=PaddingLeft,
            conditions=[Fit2Width(), Center2Center(), Top2Top()],
            xAlign=Justify, yAlign=TOP, hyphenation=True)
    return template

def makeAnimation(WGTH,WDTH,SLNT,CNTR):
    template = Template(w=W, h=H) 
    FONTSTYLE = getVarFontInstance(font, dict(wght=WGTH, wdth=WDTH, slnt=SLNT, CNTR=CNTR))
    style = dict(font=FONTSTYLE.path, fontSize=FONTSIZE, rLeading=0.8, lineHeight=LHeight, xTextAlign=Justify, textFill=(0, 0, 0,1))
    title = context.newString(lines, style=style)
    newTextBox(title, parent=template, name='Other element',  pt=PaddingTop, pr=PaddingRight, pl=PaddingLeft,
            conditions=[Fit2Width(), Center2Center(), Top2Top()],
            xAlign=Justify, yAlign=TOP, hyphenation=True)
    return template

def makeWords(startWGTH,endWGTH,startWDTH,endWDTH, startSLNT, endSLNT, startCNTR, endCNTR):
    template = Template(w=W, h=H) 
    
    linesDict = lines.split()
    print (linesDict) 
    print (range(len(linesDict)))
    s = "" 
    bs = context.newString(s)
    for i in range(len(linesDict)):
        f = i / len(linesDict)
        WGTH = startWGTH + (f * (endWGTH - startWGTH))
        WDTH = startWDTH + (f * (endWDTH - startWDTH))
        SLNT = startSLNT + (f * (endSLNT - startSLNT))
        CNTR = startCNTR + (f * (endCNTR - startCNTR))
        location = getConstrainedLocation(font, dict(wght=WGTH, wdth=WDTH, slnt=SLNT, CNTR=CNTR))
        instance = getVarFontInstance(font, location, normalize=True, cached=False, lazy=False)
        style = dict(font=instance.path, fontSize=FONTSIZE, rLeading=LHeight, xTextAlign=Justify, textFill=(0, 0, 0,1))
        title = context.newString(lines, style=style)
        bs.__add__(context.newString((linesDict[i]+add),style=style))
    newTextBox(bs, parent=template, name='Other element',  pt=PaddingTop, pr=PaddingRight, pl=PaddingLeft,
            conditions=[Fit2Width(), Center2Center(), Top2Top()],
            xAlign=Justify, yAlign=TOP, hyphenation=True)
    return template

def makeTemplate (StringContent):
    template = Template(w=W, h=H) 
    newTextBox(StringContent, parent=template, name='Other element',  pt=PaddingTop, pr=PaddingRight, pl=PaddingLeft,
            conditions=[Fit2Width(), Center2Center(), Top2Top()],
            xAlign=Justify, yAlign=TOP, hyphenation=True)
    return template

def makeDocument():
    if mode == 'Anim':
        template = makeAnimation(0,0,0,0)
    elif mode == 'Iter':
        template = makeIteration(0,0,0,0,0,0,0,0)
    elif mode == 'Words':
        template = makeWords(0,0,0,0,0,0,0,0)
        
    pages = []
    
    for i in range(frames):
        pages.append(i+1)
    
    doc = Document(title='V-F AnimIterator', w=W, h=H, originTop=False, autoPages=frames, defaultTemplate=template)

    for i in pages:
        def easeInOutQuad(n):
            if n< 0.5:
                return 2 * n**2
            else:
                n=n * 2 -1
            return -0.5 * (n*(n-2) - 1)

        def Method(start, end):
            ee = easeInOutQuad(i/frames)
            result = start+(((end-start) * ee))
            return result
        
        sWGTH = Method(WG[0],WG[1])
        eWGTH = Method(WG[2],WG[3])
        sWDTH = Method(WD[0],WD[1])
        eWDTH = Method(WD[2],WD[3])
        sSLNT = Method(SL[0],SL[1])
        eSLNT = Method(SL[2],SL[3])
        sCNTR = Method(CT[0],CT[1])
        eCNTR = Method(CT[2],CT[3])
    

    
        pageid = i + 1
        # print(pageid, sWGTH,eWGTH,sWGTH,eWDTH)
        page = doc.getPage(i)
        if mode == 'Anim':
            page.applyTemplate(makeAnimation(sWGTH,sWDTH,sSLNT,sCNTR))
        elif mode == 'Iter':
            page.applyTemplate(makeIteration(sWGTH,eWGTH,sWDTH,eWDTH, sSLNT, eSLNT, sCNTR, eCNTR))
        elif mode == 'Words':
            page.applyTemplate(makeWords(sWGTH,eWGTH,sWDTH,eWDTH, sSLNT, eSLNT, sCNTR, eCNTR))
        else:
            print ('Incorrect mode')
    doc.solve()
    return doc # Answer the doc for further doing.

d = makeDocument()
d._set_frameDuration(1/fps)
d.export()
name = mode + ' wg ' + str(WG) + 'wd' + str(WD) + 'sl' + str(SL) + 'ct' + str(CT)
print (name)
EXPORT_PATH = '_export/' + name + '-V-F' + note + '.' + ext
if saver == 'on':
    saveImage(EXPORT_PATH)