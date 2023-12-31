# Given an array arr of size N and an element k. The task is to find the count of elements in the array that appear more than n/k times.

# Example 1:

# Input:
# N = 8
# arr = [3,1,2,2,1,2,3,3]
# k = 4
# Output: 
# 2
# Explanation: 
# In the given array, 3 and 2 are the only elements that appears more than n/k times.
# Example 2:

# Input:
# N = 4
# arr = [2,3,3,2]
# k = 3
# Output: 
# 2
# Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.
# Your Task:
# The task is to complete the function countOccurence() which returns count of elements with more than n/k times appearance.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

#User function Template for python3


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        min_freq = n // k
        
        freq_map = {}
        
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        count = 0
        for key, value in freq_map.items():
            if value > min_freq:
                count += 1
        
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends