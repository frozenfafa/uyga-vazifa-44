file = open("homework/product_material.txt","r")
gap = file.readlines()
gap = list(map(lambda line: line.split(","),gap))
for i in range(len(gap)):
    gap[i][4]=gap[i][4][:-1]
gap.sort(key = lambda line: float(line[3][1:]))    
material = input("Enter the products material: ")
for i in gap:
    if material.lower() == i[2].lower() and i[4] == 'true':
        print(i)