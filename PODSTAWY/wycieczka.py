def kwota(t,nw,w,u,i,rab=0):
    return (nw+t)*(1-rab/100)+w+u+i
print(kwota(100,100,50,50,50),"zł")
print(kwota(100,100,50,50,50,25),"zł")
