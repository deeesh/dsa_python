
# send these to 2 new lists and add
def move_negative_number(arr, n):
    newarr = []
    n =[]
    for _ in arr:
        if _ < 0:
            newarr.append(_)
        else:
            n.append(_)
    e = newarr + n
    print(e)

arr = [-1, 2, 4, 8, 2, -2, -5]
n = len(arr)
move_negative_number(arr, n)


# Using Sort Function
def move_negative_number(arr, n):
    arr.sort()
    print(arr)

arr = [-1, 2, 4, 8, 2, -2, -5]
n = len(arr)
move_negative_number(arr, n)


# using Quick Sort
def move_negative_number(arr, n):
    j=0
    for i in range(0, n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1
    print(arr)
   
arr = [-1, 2, 4, 8, 2, -2, -5]
n = len(arr)
move_negative_number(arr, n)
