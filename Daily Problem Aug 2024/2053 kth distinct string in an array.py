class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        nums = {}
        for x in arr:
            if x in nums:
                nums[x]+=1
            else:
                nums[x] = 1
        
        distinct = [x for x in arr if nums[x] == 1]
        n = len(distinct)
        if n >= k:
            return distinct[k-1]
        else:
            return ""