class Solution:

    def countStr(self, n):
        res = 0
        res += 1 + (n * 2)
        res += n * ((n * n) - 1) / 2
        
        return int(res)

                
# 1 + (n * 2): This part represents the counts for strings of length 1.
# There are 1 possibility for each character ('a', 'b', 'c'), and for the next positions,
# there are 2 possibilities ('ab', 'ac', 'ba', 'bc', 'ca', 'cb').

# n * ((n * n) - 1) / 2: This part seems to represent the counts for strings of length greater than 1.
# It considers all possible combinations of 'a', 'b', and 'c' for each position,
# excluding the case where all characters are the same.



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends