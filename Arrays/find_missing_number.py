
def missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

arr_with_missing_numbers = [1,2,4,5,6]
missing_number = missing_number(arr_with_missing_numbers)
print(missing_number)

