def helix(n):
    t = [[0]*n for i in range (n)]
    i, j = 0, 0
    for k in range(1, n*n+1):
        t[i][j]=k
        if k == n*n: break
        if i<=j+1 and i+j<n-1:
            j+=1
        elif i<j and i+j>=n-1:
            i+=1
        elif i>=j and i+j>n-1:
            j-=1
        elif i>j+1 and i+j<=n-1:
             i-=1
    return t

#test
res = helix(6)
for i in res:
    print(*i)
