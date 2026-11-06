# Versão de cada marca para fundo escuro: mantém matiz e saturação, só sobe a luminosidade do que sumiria.
import sys, numpy as np
from PIL import Image
P=sys.argv[1]
def hls(rgb):
    mx=rgb.max(-1); mn=rgb.min(-1); L=(mx+mn)/2; d=mx-mn
    S=np.where(d==0,0,d/np.maximum(1-np.abs(2*L-1),1e-6))
    r,g,b=rgb[...,0],rgb[...,1],rgb[...,2]; dd=np.maximum(d,1e-6)
    H=np.where(mx==r,((g-b)/dd)%6,np.where(mx==g,(b-r)/dd+2,(r-g)/dd+4))/6
    return H,L,S
def rgb(H,L,S):
    C=(1-np.abs(2*L-1))*S; h=H*6; X=C*(1-np.abs(h%2-1)); m=L-C/2; z=np.zeros_like(H)
    k=np.floor(h).astype(int)%6
    R=np.choose(k,[C,X,z,z,X,C]); G=np.choose(k,[X,C,C,X,z,z]); B=np.choose(k,[z,z,X,C,C,X])
    return np.stack([R+m,G+m,B+m],-1)
for f in ["arqrede","base-de-projetos","andreza-fama","polyana-diogenes","emily-franca","gdg-natal"]:
    im=Image.open(f"{P}/logos/{f}.png").convert("RGBA"); a=np.asarray(im).astype(np.float64)/255
    H,L,S=hls(a[...,:3])
    neutro=S<.22
    L2=np.where(neutro,np.where(L<.72,.95,L),np.maximum(L,.64))
    S2=np.where(neutro,S*.4,np.clip(S*1.05,0,.9))
    alfa=a[...,3]
    if f=="gdg-natal": alfa=alfa*np.where(neutro,np.clip((.97-L)/.12,0,1),1)
    out=np.dstack([rgb(H,L2,S2),alfa])
    Image.fromarray((np.clip(out,0,1)*255+.5).astype(np.uint8),"RGBA").save(f"{P}/logos/escuro/{f}.png",optimize=True)
# prova lado a lado no fundo escuro
fs=["arqrede","base-de-projetos","andreza-fama","polyana-diogenes","emily-franca","gdg-natal"]
fol=Image.new("RGB",(1300,420),(11,12,14)); x=20; y=20
for f in fs:
    v=Image.open(f"{P}/logos/escuro/{f}.png").convert("RGBA"); s=90/v.height; v=v.resize((int(v.width*s),90))
    if x+v.width>1280: x=20; y+=130
    fol.paste(v,(x,y),v); x+=v.width+50
fol.save(sys.argv[2])
