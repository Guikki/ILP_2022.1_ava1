ida =int(input())
for i in range (ida):
    preco=0
    prod =int(input())
    for j in range (prod):
        pu, quant = input().split()
        pu = float(pu)
        quant = float(quant)
        preco += pu*quant
    print ("R$", "%.2f"% (preco))
