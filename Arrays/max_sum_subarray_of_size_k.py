# GFG
# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

# NOTE*: A subarray is a contiguous part of any given array.

# Example 1:

# Input:
# N = 4, K = 2
# Arr = [100, 200, 300, 400]
# Output:
# 700
# Explanation:
# Arr3  + Arr4 =700,
# which is maximum.
# Example 2:

# Input:
# N = 4, K = 4
# Arr = [100, 200, 300, 400]
# Output:
# 1000
# Explanation:
# Arr1 + Arr2 + Arr3 + Arr4 =1000,
# which is maximum.
# Your Task:

# You don't need to read input or print anything.
# Your task is to complete the function maximumSumSubarray() which takes the integer K, 
# vector Arr with size N, containing the elements of the array 
# and returns the maximum sum of a subarray of size K.


#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        
        maxi = sum(Arr[:K])
        current_sum = maxi
        
        for i in range(K, N):
            current_sum = current_sum + Arr[i] - Arr[i-K]
            maxi = max(maxi, current_sum)
            
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends