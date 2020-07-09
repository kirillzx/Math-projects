def mirror(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1):
            x = array[i][j]
            array[i][j] = array[n-j-1][n-i-1]
            array[n-j-1][n-i-1] = x
    return array

#test1
a = [[1,2,3],[4,5,6],[7,8,9]]
for r in a:
    print(*r)
print("\nResult")
res = mirror(a)
for r in res:
    print(*r)
