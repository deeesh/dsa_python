class Solution:
    def doUnion(self, a,b,n,m):
        newarr = a + b
        c = set(newarr)
        return c

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().strip().split()]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution
        print(ob.doUnion(a, b, n, m))

