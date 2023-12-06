def RightRotate(a, n, k):
	k = k % n
	# k=1 k=2 k=3 k=4 k=5 k=6 k = 7 n=7
	# i=0 1 2 3 4 5 6 7
	for i in range(0, n):
		# i=0 k=3
		if(i < k):
			# Printing rightmost kth elements, a[7 + 0 - 3] = a[4] (5) , a[7+1-3] = a[5] (8), a[7+2 - 3] = a[6] (10)
			#  arr = [5, 8, 10,]
			print(a[n + i - k], end = " ")
		else:
			# Prints array after 'k' elements
			#  arr = a[3 - 3] = a[0] (1), a[4-3] = a[1] (2), a[5-3]=a[2] (3), a[6-3]=a[3] (4)
			print(a[i - k], end = " ")
	print("\n")

Array = [ 1, 2, 3, 4, 5, 8, 10 ]
N = len(Array)
K = 3
RightRotate(Array, N, K)

