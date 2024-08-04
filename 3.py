file = open("homework/product_material.txt","r")
gap = file.readlines()
gap = list(map(lambda line: line.split(","),gap))
for i in range(len(gap)):
    gap[i][4]=gap[i][4][:-1]
for i in gap:
    if i[4] == 'false' and float(i[3][1:]) < 1000:
        print(i[0],i[2])    