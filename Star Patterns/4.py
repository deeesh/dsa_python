# Number Pattern 
# 1
# 23
# 456
# 78910

def print_numbers(num_rows):
    num = 1
    for i in range(num_rows):
        for j in range(i+1):
            print(num, end="")
            num = num+1
        print("\r")
num_rows = int(input())
print_numbers(num_rows)


# 1
# 22
# 333
# 4444
# Isme row ki value k according chalega
def print_numbers(num_rows):
    for i in range(num_rows):
        for j in range(i+1):
            print(i+1, end="")
        print("\r")
num_rows = int(input())
print_numbers(num_rows)


# 1
# 12
# 123
# 1234
# Isme J ki value Increment ho rhi h
def print_numbers(num_rows):
    for i in range(num_rows):
        for j in range(i+1):
            num = j+1
            print(num, end="")
            num = num+1
        print("\r")


num_rows = int(input())
print_numbers(num_rows)