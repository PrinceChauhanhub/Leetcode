class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        arr = []
        for i in range(n):
            ssum = 0
            for j in range(i,n):
                ssum += nums[j]
                arr.append(ssum)
        arr.sort()
        sum = 0
        for x in range(left-1,right):
            sum += arr[x]
        return sum % MOD