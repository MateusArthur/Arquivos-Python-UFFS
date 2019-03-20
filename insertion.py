l = [5,3,4,8,9,1,2]
for x in range(len(l)-1):
	for j in range(len(l)-1):
		armz = l[j]
		if l[j] > l[j+1]:
			l[j] = l[j+1]
			l[j+1] = armz

for x in range(len(l)):
	print(l[x])