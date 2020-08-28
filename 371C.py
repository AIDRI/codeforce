string = input()
nb = 0
ns = 0
nc = 0
 
for i in string:
	if i == "B":
		nb += 1
	elif i == "S":
		ns += 1
	else:
		nc += 1
 
 
b, s, c = map(int, input().split())
#print(b, s, c)
pb, ps, pc = map(int, input().split())
#print(pb, ps, pc)
 
tr = int(input())
rc = nb*pb + nc*pc + ns*ps
l = 0
r = int(10e12 + 1)
l = -1

while (l<r-1):
	m = (l+r)//2
 
	if max(0, pb*(nb*m-b))+max(0, pc*(nc*m-c))+max(0, ps*(ns*m-s)) <= tr:
		temp_ans = m
		l = m
	else:
		r = m
 
print(temp_ans)
