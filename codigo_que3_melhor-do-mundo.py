mgols=0
fera=0
while mgols < 101:
    jog,gols=input().split()
    gols= int(gols)
    if gols>=1000:
        break 
    elif gols > 45:
        mgols=gols
        fera=jog 
print(fera,"melhor do mundo com",mgols, "gols.")
