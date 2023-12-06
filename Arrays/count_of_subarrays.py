# GFG 
def countSubarray(arr, n, k):
        count = 0
        result = 0
    
        for i in range(n):
            if arr[i] > k:
                count = 0
            else:
                count += 1
                result += count
        print(n * (n + 1) // 2 - result)
        return n * (n + 1) // 2 - result

# arr = [8 ,-2, -2, 0, 8, 0, -6, -8, -6, -1]
arr=[1,2,3,4]
n=len(arr)
k=1
countSubarray(arr, n, k)
