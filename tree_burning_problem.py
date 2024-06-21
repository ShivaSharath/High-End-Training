n=int(input())
#a=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
a=[list(map(int,input().split())) for _ in range(n)]
i,j=map(int,input().split())
def burn(i, j):
    if (not (0<=i<n and 0<=j<n)) or a[i][j]==0 :
        return
    a[i][j]=0
    burn(i, j+1)
    burn(i+1, j)
    burn(i-1, j)
    burn(i, j-1)
burn(i-1, j-1)
print(sum([sum(row) for row in a]))
