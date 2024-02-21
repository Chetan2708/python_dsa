class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        count = 0
        for i in range(0,len(word),k):
            a = word[i:]
            if a==word[:len(a)] and count!=0:
                break
            count+=1
        return (count)
        