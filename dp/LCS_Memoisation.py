# Longest common subsequence
#Bottom - up ( time - O(M*N))
# Space - O(M*N)+O(M+N)

def fun(a, b,  i, j , dp):
    if i <0 or j<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    elif a[i] == b[j]:
        dp[i][j]=  1+(fun(a, b, i-1, j-1 , dp))
    else:
        
        dp[i][j]= max(fun(a, b, i, j-1 ,dp), fun(a, b, i-1, j , dp))
    return dp[i][j]


a = 'abcde'
b = 'bce'
n=len(a)
m=len(b)
dp = [[-1]*(m+1) for i in range(n+1)]

print(fun(a, b , n-1 , m-1 , dp))



