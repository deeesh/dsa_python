
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