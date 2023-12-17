#User function Template for python3
class Solution:	
    def findMaxSum(self,arr, n):
        if n == 0:
                return 0
        if n == 1:
            return arr[0]

        incl = arr[0]
        excl = 0

        for i in range(1, n):
            new_excl = max(incl, excl)
            incl = excl + arr[i]
            excl = new_excl

        return max(incl, excl)



#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends