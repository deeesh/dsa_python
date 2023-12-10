# Given an array of integers. 
# Find if there is a subarray (of size at-least one) with 0 sum.
# You just need to return true/false depending upon whether there is a subarray present with 0-sum or not.
# Printing will be taken care by the driver code.

#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        cumulative_sums = set()
        current_sum = 0
        for num in arr:
            current_sum += num
            if current_sum in cumulative_sums or current_sum == 0:
                return True
            cumulative_sums.add(current_sum)
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends