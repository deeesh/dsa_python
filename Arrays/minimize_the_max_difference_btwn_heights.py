# GFG
# Given the heights of N towers and a value of K,
# Either increase or decrease the height of every tower by K (only once) where K > 0. 
# After modifications, the task is to minimize the difference between the heights of the longest and the shortest tower and output its difference.

# Input:
# K = 3, N = 5
# Arr[] = {3, 9, 12, 16, 20}
# Output:
# 11
# Explanation:
# The array can be modified as
# {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}. 
# The difference between 
# the largest and the smallest is 17-6 = 11. 


# The idea is to increase the first i towers by k and 
# decrease the rest tower by k after sorting the heights, 
# then calculate the maximum height difference.
# This can be achieved using sorting.

class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        result = arr[n- 1] - arr[0]
        
        tempmin = arr[0]
        tempmax = arr[n - 1]
        
        for i in range(1, n):
            if arr[i]<k:
                continue
            tempmin = min(arr[0] + k, arr[i] - k)
            tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
            
            result = min(result, tempmax - tempmin)
            
        return result
                            

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
