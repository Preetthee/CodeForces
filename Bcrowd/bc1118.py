x=0
m,n,o=0,0,1
while(x!=2):
    x = float(input())
    if 0<x<11 and o==1:
        n+=1
        m+=x
        if n==2:
            print(f"media = {m/2}")
            m,n,o=0,0,2
    elif x!=1 and 0==2:
        print("novo calculo (1-sim 2-nao)")
    elif x!=1 and 0==2:
        print("novo calculo (1-sim 2-nao)")
    else:
        print("nota invalida")