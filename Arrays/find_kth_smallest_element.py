# Using Brute FOrce Method
def find_kth_element(arr, k):
    n = len(arr)-1
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[k-1]


arr = [7, 10, 4, 3, 10, 15]
k = 3
find_kth_element(arr, k)
print(find_kth_element(arr, k))

# Using Heap Mwthod
# import heapq

# def find_kth_element(arr, k):
#     heap = []  
#     for num in arr:  
#         heapq.heappush(heap, num)  
          
#         kth_smallest = None  
#         for _ in range(k+1):  
#             kth_smallest = heapq.heappop(heap)  
          
#         return kth_smallest  


# arr = [7, 10, 4, 3, 10, 15]
# k = 3
# find_kth_element(arr, k)
# print(find_kth_element(arr, k))