#Time Complexity -> O(n)
#space Complexity -> O(1)

# approach -> try to count the number the times we need to sum the same number in the answer
#          means->count the frequency of each number
            
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        prevEvensum=0
        prevOddsum=0
        for i , val in enumerate(arr):
            currOddsum = prevEvensum + (i // 2 + 1) * val
            currEvensum = prevOddsum +((i + 1) // 2)*val
            ans+=currOddsum

            prevEvensum = currEvensum
            prevOddsum = currOddsum

        return ans

