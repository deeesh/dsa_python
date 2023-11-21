# Using Slicing
def reversearray(array_input):
    new_array = array_input[::-1]
    print(new_array)

array_input = [2, 4, 5, 8, 3, 1]
reversearray(array_input)

# Using Swapping While Loop

def reversearray(array_input):
    left = 0
    right = len(array_input) - 1
    while(left<right):
        temp = array_input[left]
        array_input[left] = array_input[right]
        array_input[right] = temp
        left += 1
        right -= 1
    return array_input


array_input = [2, 4, 5, 8, 3, 1]
reversearray(array_input)
