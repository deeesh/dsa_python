
def duplicate(number):
    duplicate_list = []
    unique_list = []
    for i in number:
        if i not in unique_list:
            unique_list.append(i)
        elif i not in duplicate_list:
            duplicate_list.append(i)


    print(duplicate_list)
        
number = [1, 2, 3, 3, 5, 7]
duplicate(number)

# Sort the Array and iterate to n-1 and check if nums[i]==nums[i+1] and return nums[i]
def findDuplicate(nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return nums[i]
                
nums = [1,3,4,2,2]
findDuplicate(nums)