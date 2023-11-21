# Dutch National Flag ka dash dash

# Algorithm: 
# 1. Keep three indices low = 1, mid = 1 and high = N and there are four ranges, 1 to low
# (the range containing 0), low to mid (the range containing 1), mid to high (the range
# containing unknown elements) and high to N (the range containing 2).
# 2. Traverse the array from start to end and mid is less than high. (Loop counter is i)
# 3. If the element is 0 then swap the element with the element at index low and update
# low = low + 1 and mid = mid + 1
# 4. If the element is 1 then update mid = mid + 1
# 5. If the element is 2 then swap the element with the element at index high and
# update high = high – 1 and update i = i – 1. As the swapped element is not processed
# 6. Print the output array.



class Solution:
    def sort012(self, arr, n):
        low, mid, high = 0, 0, n-1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low+=1
                mid+=1
            elif arr[mid] == 1:
                mid+=1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

