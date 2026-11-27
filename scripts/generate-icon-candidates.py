# -*- coding: utf-8 -*-
"""Thistle & Terrace Theme - icon candidates. Code-drawn, transparent, flat."""
import io, math, os
from PIL import Image, ImageDraw, ImageFont

S=3; W=1024
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,"assets","logo-candidates")

PLUM=(126,78,136,255)      # #7E4E88  corrected deep plum
LILAC=(175,142,177,255)    # #AF8EB1  lilac
SAGE=(172,207,197,255)     # #ACCFC5  corrected sage
CREAM=(241,227,196,255)    # #F1E3C4  cream
INK=(46,31,49,255)

LIGHT_BG=(199,190,205,255)
DARK_BG=(46,31,49,255)
LIGHT_INK=(46,31,49,255)
DARK_INK=(241,227,196,255)
FONT_DIR=r"C:\Windows\Fonts"

def font(n,s):
    try: return ImageFont.truetype(os.path.join(FONT_DIR,n),s)
    except Exception: return ImageFont.load_default()
def scr(p): return (p[0]*S,p[1]*S)
def wd(v): return max(1,int(round(v*S)))
def canvas(): return Image.new("RGBA",(W*S,W*S),(0,0,0,0))
def finish(i): return i.resize((W,W),Image.LANCZOS)
def poly(d,pts,c): d.polygon([scr(p) for p in pts],fill=c)
def disc(d,ctr,r,c): d.ellipse([ctr[0]*S-r*S,ctr[1]*S-r*S,ctr[0]*S+r*S,ctr[1]*S+r*S],fill=c)
def rrect(d,b,r,c): d.rounded_rectangle([b[0]*S,b[1]*S,b[2]*S,b[3]*S],radius=r*S,fill=c)
def line(d,pts,c,w): d.line([scr(p) for p in pts],fill=c,width=wd(w),joint="curve")
def bez(p0,p1,p2,n=48):
    out=[]
    for i in range(n+1):
        t=i/n;u=1-t
        out.append((u*u*p0[0]+2*u*t*p1[0]+t*t*p2[0],u*u*p0[1]+2*u*t*p1[1]+t*t*p2[1]))
    return out

def petal(d,cx,cy,ang,ln,col):
    right=bez((0,0),(ln*0.5,-ln*0.4),(0,-ln))
    left=bez((0,-ln),(-ln*0.5,-ln*0.4),(0,0))
    ca,sa=math.cos(ang),math.sin(ang)
    poly(d,[(cx+x*ca-y*sa,cy+x*sa+y*ca) for x,y in right+left],col)

def terrace(d,x0,x1,y0,step,h,cols):
    for i,c in enumerate(cols):
        y=y0+i*step
        d.rectangle([x0*S,y*S,x1*S,(y+h)*S],fill=c)

def cand_thistle():
    img=canvas();d=ImageDraw.Draw(img)
    line(d,[(512,900),(512,520)],INK,20)
    for a in (-math.pi/2, -math.pi/2+math.pi/4, -math.pi/2-math.pi/4):
        petal(d,512,470,a,250,PLUM)
    for a in (-1.9,-1.24):
        petal(d,512,470,a,180,LILAC)
    disc(d,(512,470),80,SAGE)
    leaf(d,512,700,math.radians(-150),170,70,LILAC) if False else None
    petal(d,500,690,math.radians(-115),160,70) if False else None
    return finish(img)

def cand_terrace():
    img=canvas();d=ImageDraw.Draw(img)
    rrect(d,(240,160,784,864),36,CREAM)
    cols=(PLUM,LILAC,SAGE,CREAM)
    for i,c in enumerate(cols):
        y=210+i*158
        d.rectangle([280*S,y*S,744*S,(y+130)*S],fill=c)
    return finish(img)

def cand_arch_terrace():
    img=canvas();d=ImageDraw.Draw(img)
    r=(724-300)//2; cx=512
    d.pieslice([300*S,180*S,724*S,(180+2*r)*S],180,360,fill=PLUM)
    d.rectangle([300*S,(180+r)*S,724*S,860*S],fill=PLUM)
    terrace(d,300,724,540,100,90,(LILAC,SAGE,CREAM))
    return finish(img)

def cand_steps():
    img=canvas();d=ImageDraw.Draw(img)
    cols=(PLUM,LILAC,SAGE,CREAM)
    for i,c in enumerate(cols):
        x=180+i*175
        rrect(d,(x,420-i*80,x+175,840),18,c)
    return finish(img)

def cand_wreath():
    img=canvas();d=ImageDraw.Draw(img)
    cols=(PLUM,LILAC,SAGE,CREAM,PLUM,LILAC)
    for i,c in enumerate(cols):
        a=-math.pi/2+i*math.pi/3
        petal(d,512+230*math.cos(a),512+230*math.sin(a),a+math.pi/2,160,c)
    disc(d,(512,512),96,CREAM)
    return finish(img)

def cand_bloom_terrace():
    img=canvas();d=ImageDraw.Draw(img)
    terrace(d,180,844,560,80,72,(PLUM,LILAC,SAGE,CREAM))
    line(d,[(512,560),(512,420)],INK,16)
    for a in (-math.pi/2,-math.pi/2+0.7,-math.pi/2-0.7):
        petal(d,512,410,a,190,PLUM)
    disc(d,(512,410),62,LILAC)
    return finish(img)

CANDIDATES=[
 ("01","thistle",cand_thistle),("02","terrace-bands",cand_terrace),
 ("03","arch-terrace",cand_arch_terrace),("04","steps",cand_steps),
 ("05","wreath",cand_wreath),("06","bloom-terrace",cand_bloom_terrace),
]

def centered(d,ctr,text,f,col):
    b=d.textbbox((0,0),text,font=f)
    d.text((ctr[0]-(b[2]-b[0])/2-b[0],ctr[1]-(b[3]-b[1])/2-b[1]),text,font=f,fill=col)

def sheet(icons,bg,ink,path):
    cw,ch=420,540;m,g,h=40,26,118
    sw=m*2+cw*3+g*2;sh=m+h+ch*2+g+m
    im=Image.new("RGBA",(sw,sh),bg);d=ImageDraw.Draw(im)
    ft=font("segoeuib.ttf",40);fn=font("segoeuib.ttf",30)
    fna=font("segoeui.ttf",26);fs=font("segoeui.ttf",20)
    centered(d,(sw/2,m+34),"THISTLE & TERRACE THEME",ft,ink)
    centered(d,(sw/2,m+82),"icon candidates",fs,ink)
    for i,(num,name,icon) in enumerate(icons):
        r,c=divmod(i,3);gx=m+c*(cw+g);gy=m+h+r*(ch+g)
        im.alpha_composite(icon.resize((260,260),Image.LANCZOS),(gx+(cw-260)//2,gy+30))
        centered(d,(gx+cw/2,gy+330),num,fn,ink)
        centered(d,(gx+cw/2,gy+372),name,fna,ink)
        centered(d,(gx+cw/2,gy+404),"1024 x 1024  PNG",fs,ink)
    save(im.convert("RGB"),path)

def strip(icons,path):
    sz,g,m=150,18,30
    sw=m*2+sz*len(icons)+g*(len(icons)-1);sh=m*2+sz+34
    im=Image.new("RGBA",(sw,sh),LIGHT_BG);d=ImageDraw.Draw(im)
    f=font("segoeuib.ttf",20)
    for i,(num,_n,icon) in enumerate(icons):
        x=m+i*(sz+g)
        im.alpha_composite(icon.resize((sz,sz),Image.LANCZOS),(x,m))
        centered(d,(x+sz/2,m+sz+16),num,f,LIGHT_INK)
    save(im.convert("RGB"),path)

def save(img,path):
    buf=io.BytesIO();img.save(buf,format="PNG")
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"wb") as fh: fh.write(buf.getvalue())

def main():
    os.makedirs(OUT,exist_ok=True)
    icons=[]
    for num,name,fn in CANDIDATES:
        icon=fn();box=icon.getbbox()
        if box is None: raise AssertionError(name+" empty")
        if box[0]<70 or box[1]<70 or box[2]>954 or box[3]>954:
            raise AssertionError(name+" out of safe area: "+str(box))
        save(icon,os.path.join(OUT,"%s-%s.png"%(num,name)))
        print("wrote",num,name,box)
        icons.append((num,name,icon))
    sheet(icons,LIGHT_BG,LIGHT_INK,os.path.join(OUT,"contact-light.png"))
    sheet(icons,DARK_BG,DARK_INK,os.path.join(OUT,"contact-dark.png"))
    strip(icons,os.path.join(OUT,"inline-strip.png"))
    print("wrote contact sheets")

if __name__=="__main__": main()

