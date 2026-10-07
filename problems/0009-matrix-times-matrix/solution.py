def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0])==len(b):
        temple=[[0 for k in b[0]] for l in a]
        for i in range(len(a)):
            for j in range(len(b[0])):
                temp=0
                for k in range(len(a[0])):
                    temp+=a[i][k]*b[k][j]
                temple[i][j]=temp
        return temple
    else:
        return -1