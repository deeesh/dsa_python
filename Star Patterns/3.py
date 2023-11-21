# Triangle Full
#       *  
#     *  *  
#   *  *  *  
# *  *  *  *  

def print_triangle(n):
    k = n-1
    for i in range(n):
        for j in range(k):
            print(" ", end=" ")
        k = k-1
        for l in range(i+1):
            # Star k aage space lga dia soi chal gya :-> waah 
            print("* ", end=" ")
        print("\r")

n = int(input("Enter No. Of Rows for Triangle"))
print_triangle(n)
