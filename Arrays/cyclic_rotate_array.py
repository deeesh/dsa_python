def rotate(arr,n):
    #  Last Element will be (n-1)th element
    last_element = arr[n-1]
    #  Iterate loop from (n-1)th element to 0th Element
    # i = 4 
    for i in range(n-1, 0, -1):
        # arr[4] = arr[3]
        arr[i] = arr[i-1]
    arr[0] = last_element
    
arr = [1,2,3,4,5]
n = len(arr)
print(rotate(arr, n))