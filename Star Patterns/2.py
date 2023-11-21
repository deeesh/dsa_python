# Print Right Triangle Star Pattern
#       * 
#     * * 
#   * * * 
# * * * * 

def print_star(n):
    k = n-1
    for i in range(n):
        for j in range(k):
            print(" ", end=" ")
        k = k-1
        for l in range(i+1):
            print("*", end=" ")
        print("\r")


n = int(input("Enter No. of rows you want to print: "))
print_star(n)
