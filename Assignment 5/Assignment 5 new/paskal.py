listPascal = []
def KhayyamPascalTriangle():
    for i in range(4):
        listPascal.append([1]*(i+1))
        for j in range(1, i):
            listPascal[i][j] = listPascal[i-1][j-1] + listPascal[i-1][j]
    return listPascal
num = KhayyamPascalTriangle()
for i in num:
    print(i)