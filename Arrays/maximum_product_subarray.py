def kadaneAlgo(arr):
    maxi = mini = result = arr[0]
    for i in arr[1:]:
        if i<0:
            maxi, mini = mini, maxi
        maxi = max(i, i*maxi)
        mini = min(i, i*mini)
    result = max(result, maxi)
    print(result)
    return result

arr = [8 ,-2, -2, 0, 8, 0, -6, -8, -6, -1]
kadaneAlgo(arr)
