n = int(input())
events = list(input())

output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
io = 0

for i in events:
	io = 0
	ior = 9
	if i == "L":
		while output[io] == "1":
			io += 1
		output[io] = "1"
	elif i == "R":
		while output[ior] == "1":
			ior -= 1
		output[ior] = "1"
	else:
		output[int(i)] = "0"

string = ""
for i in output:
	string += str(i)
	
print(string)