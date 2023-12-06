
# ! Kadane's Algorithm --> EASY --> O(n) complexity
# initially sum = 0 and maxi = arr[0] (update while iterating)
# sum = sum+arr[i] (current element)
# maxi = update --> max(maxi, sum)
# if sum < 0, sum = 0


def kadaneAlgo(arr):
    n = len(arr)
    sum = 0
    maxi = arr[0]

    for i in range(0, n):
        sum += arr[i]
        maxi = max(maxi, sum)

        if sum < 0:
            sum = 0
    print(maxi)
    return maxi

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
kadaneAlgo(arr)



