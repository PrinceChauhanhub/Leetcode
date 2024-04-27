# Time Complexity --> O(n)
# Space Complexity --> O(1)

#Approach --> calculated the sum of all diagonal element and then subtract the mid element of the array according to the size of array

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        primary=0
        secondary=0
        for i in range(n):
            primary += mat[i][i]
        for i in range(n):
            secondary += mat[i][n-i-1]
        if(n%2==0):
            return primary + secondary 
        else:
            return primary + secondary - mat[n//2][n//2]
