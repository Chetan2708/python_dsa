class Solution:
    def reverseWords(self, s: str) -> str:
        i, j , res , n = 0 , 0  , "", len(s)

        while i < n:
            while( i < n and s[i] == " "): i+=1
            if ( i>=n ): break
            j=i+1
            while (j < n and s[j] != " ") : j+=1
            sub= s[i:j]
            if (len(res) == 0) : res = sub
            else : res = sub + " " +res
            i=j+1
        return res

  