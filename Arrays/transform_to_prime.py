#User function Template for python3



class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
    def minNumber(self, arr,n):
        array_sum = sum(arr)
        if self.is_prime(array_sum):
            return 0
        for i in range(1, array_sum+1):
            if self.is_prime(array_sum+i):
                return i
           



#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends