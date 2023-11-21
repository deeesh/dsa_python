# t = int(input())
# for i in range(1, t):
#     print(i*('*'))

# Left Half Pyramid
num_rows = int(input())
k=1
for i in range(0, num_rows):
    for j in range(0, k):
        print("*", end=' ')
    k=k+1
    print()
