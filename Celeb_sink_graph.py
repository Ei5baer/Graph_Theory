import random

n = 10
A = [[ ( 1 if (j<=i) else 0)  for i in range(n) ] for j in range (n) ]

#n = A.size()
cs = [0 for i in range(n)]

for c in range(n):
	for r in range(n):
		cs[c]=cs[c]+A[r][c]

flg = False


for j in range (n):
	if (cs[j]>=1):
		badflag = True
		

	else:
		if (sum(A[j]) == n-1):
			print (j )
			badflag = False
			print (" is the celeb node")
			flg = True

if (badflag == True and flg == False):
	print ("No node found")