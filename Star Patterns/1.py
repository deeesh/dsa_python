# Print Left Triangle Star Pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

def print_star(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print("\r")

n = int(input("Enter No. of star you want to print: "))
print_star(n)