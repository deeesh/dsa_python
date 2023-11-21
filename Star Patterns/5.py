# Character pattern 
# A 
# A A 
# A A A 
# A A A A 

def print_char(rows):
    ch = 65
    for _ in range(rows):
        for j in range(_+1):
            print(chr(ch), end=" ")
        print("\r")
num_rows = int(input("Enter No. of rows"))
print_char(num_rows)

# A 
# B C 
# D E F 
# G H I J 
def print_char(rows):
    ch = 65
    for _ in range(rows):
        for j in range(_+1):
            print(chr(ch), end=" ")
            ch += 1
        print("\r")
num_rows = int(input("Enter No. of rows"))
print_char(num_rows)

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
def print_char(rows):
    ch = 65
    for _ in range(rows):
        for j in range(_+1):
            print(chr(ch), end=" ")
        ch += 1
        print("\r")
num_rows = int(input("Enter No. of rows"))
print_char(num_rows)

# A 
# A B 
# A B C 
# A B C D 
def print_char(rows):
    ch = 65
    for _ in range(rows):
        for j in range(_+1):
            print(chr(ch), end=" ")
            ch += 1
        ch=65
        print("\r")
num_rows = int(input("Enter No. of rows"))
print_char(num_rows)

#         A  
#       A  B  
#     A  B  C  
#   A  B  C  D  
# A  B  C  D  E  
def print_char(rows):
    ch = 65
    k = rows - 1
    for _ in range(rows):
        for l in range(k):
            print(" ", end=" ")
        k = k-1
        for j in range(_+1):
            print(chr(ch) + " ", end=" ")
            ch += 1
        ch=65
        print("\r")
num_rows = int(input("Enter No. of rows"))
print_char(num_rows)