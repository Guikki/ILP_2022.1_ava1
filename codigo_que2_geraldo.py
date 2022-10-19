cinto,pocao = input().split() 
cinto = int(cinto)
maior=0

for i in range (cinto):
        combo=0
        poder=input().split()
        poder=[int(a) for a in poder]

        for y in range (len(poder)):
            combo=combo+poder[y]
            if combo>maior:
                maior=combo
print(combo)
