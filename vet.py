l = [5,3,4,8,9,1,2]
n = []
for i in range(len(l)):
	valor = min(l)
	l.remove(valor)
	n.append(valor)

for x in range(len(n)):
	print(n[x])
