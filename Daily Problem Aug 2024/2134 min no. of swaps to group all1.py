class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        count_ones = 0
        for x in nums:
            if x == 1:
                count_ones+=1

        new_nums = nums + nums

        max_ones_in_window = sum(new_nums[:count_ones])
        current_ones = max_ones_in_window

        for i in range(1, n):
            current_ones = current_ones - new_nums[i - 1] + new_nums[i + count_ones - 1]
            max_ones_in_window = max(max_ones_in_window, current_ones)

        min_swaps = count_ones - max_ones_in_window
        return min_swaps