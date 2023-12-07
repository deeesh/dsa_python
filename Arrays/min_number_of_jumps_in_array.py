#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        if n == 0 or arr[0] == 0:
            return -1
        
        if n == 1:
            return 0
    
        jumps = 0  # Number of jumps needed to reach the current position
        current_max_reach = 0  # The farthest index that can be reached with the current number of jumps
        next_max_reach = 0  # The farthest index that can be reached with one more jump
    
        for i in range(n - 1):
            next_max_reach = max(next_max_reach, i + arr[i])
    
            if i == current_max_reach:
                jumps += 1
                current_max_reach = next_max_reach
    
                if current_max_reach >= n - 1:
                    return jumps
    
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends