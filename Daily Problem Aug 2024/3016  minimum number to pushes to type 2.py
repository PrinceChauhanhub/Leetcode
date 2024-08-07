class Solution:
    def minimumPushes(self, word: str) -> int:
        mp = [0] * 26        
        for ch in word:
            mp[ord(ch) - ord('a')] += 1  
        mp.sort(reverse=True)
        
        ans = 0
        for i in range(26):
            ans += mp[i] * ((i // 8) + 1)
        
        return ans