# Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s. Output your answer modulo 109 + 7.

# Example 1:

# Input:
# N = 3
# Output: 5
# Explanation:
# 5 strings are (000,
# 001, 010, 100, 101).
# Example 2:

# Input:
# N = 2
# Output: 3
# Explanation: 
# 3 strings are (00,01,10).
# Your Task:
# You don't have to print answer or take inputs. Complete the function countStrings() which takes single integer n, as input parameters and returns an integer denoting the answer. 

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


#User function Template for python3
class Solution:
     def countStrings(self,n):
        MOD = 10**9 + 7
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = (a + b) % MOD, a % MOD
        return (a + b) % MOD
    	
#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends