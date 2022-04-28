listPascal = []
def KhayyamPascalTriangle(repeat):
    for i in range(repeat):
        listPascal.append([1]*(i+1))
        for j in range(1, i):
            listPascal[i][j] = listPascal[i-1][j-1] + listPascal[i-1][j]
    return listPascal
num = KhayyamPascalTriangle(int(input("Enter Number: ")))
print(num)
for i in num:
    print(i)