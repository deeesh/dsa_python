# Using Inbuilt Sort Funtion 
def find_max_min_array(arr):
    arr.sort()
    min = arr[0]
    max = arr[-1]
    return min, max

arr = [22, 14, 8, 17, 35, 3]
find_max_min_array(arr)
print(find_max_min_array(arr))

# Using Statndard Method 
def find_max_min_array(arr):
    # Dono min, max ko arr[0] maan lia fir iterate kia loop
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)-1):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    print(min, "MIN")
    print(arr, "ARR")
    print(max, "MAX")



arr = [22, 14, 8, 17, 35, 3, 9, 90, 69, 54]
find_max_min_array(arr)
# print(find_max_min_array(arr))