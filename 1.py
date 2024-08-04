file = open("homework\product_material.txt",'r')
gap = file.readlines()
for i in range(len(gap)):
    gap[i] = gap[i].split(",")
    if float(gap[i][3][1:]) > 500 and float(gap[i][3][1:]) < 1000:
        print(gap[i][0],gap[i][2])      
