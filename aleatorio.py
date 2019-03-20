from random import randint
l = [5,3,4,8,9,1,2]
o = []

for i in range(len(l)-1):
	r = randint(0, len(l)-1)
	o.append(l[r])
	del(l[r])

for x in range(len(o)):
	print(o[x])