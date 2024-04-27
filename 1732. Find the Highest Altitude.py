#Time Complexity --> O(n)
#space complexity --> O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        val=0
        sum=0
        for x in gain:
            sum+=x
            if(sum>val):
                val=sum
        return val
