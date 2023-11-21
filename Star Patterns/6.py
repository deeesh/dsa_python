#Inverted half pyramid
# ********* 
# ******** 
# ******* 
# ****** 
# ***** 
# **** 
# *** 
# ** 
# * 

def print_pattern(num_rows):
    for _ in range(num_rows):
        for j in range(num_rows):
            print(num_rows*"*", end=" ")
            num_rows = num_rows-1
            print("\r")
num_rows = int(input("Enter No. of rows:"))
print_pattern(num_rows)


# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

def print_pattern(num_rows):
    for _ in range(num_rows):
        for j in range(_+1):
            print("*", end=" ")
        print("\r")
num_rows = int(input("Enter No. of rows:"))
print_pattern(num_rows)

# * * * *  
#   * * *  
#     * *  
#       *  
# Inverted triangle
def print_pattern(num_rows):
    for _ in range(0, num_rows):
        for l in range(0, _):
            print(" ", end=" ")
        for l in range(0, num_rows - _):
            print("*", end=" ")
        print(" ")
num_rows = int(input("Enter No. of rows:"))
print_pattern(num_rows)
