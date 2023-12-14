# Given a fence with n posts and k colors, find out the number of ways of painting the fence so that not more than two consecutive posts have the same colors. Since the answer can be large return it modulo 109 + 7.

# Example 1:
# Input:
# n = 3
# k = 2 
# Output: 6

# Example 2:

# Input:
# n = 2
# k = 4 
# Output: 16
# Explanation: 
# After coloring first post with
# 4 possible combinations, you can still color
# next posts with all 4 colors. Total possible 
# combinations will be 4x4=16

# Your Task:
# Since, this is a function problem. You don't need to take any input or print anything, as it is already accomplished by the driver code. You just need to complete the function countWays() that takes n and k as parameters and returns the number of ways in which the fence can be painted (modulo 109 + 7).

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

#User function Template for python3

class Solution:
    def countWays(self,n,k):
        MOD = 10**9 + 7
        
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same, diff = k, k * (k - 1)
        for i in range(3, n + 1):
            same, diff = diff, (same + diff) * (k - 1)%MOD
        return (same + diff) % MOD
        



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends