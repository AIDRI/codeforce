def prefix_function(s):
    p = [0]
    n = len(s)
    for i in range(1, n):
        j = p[i - 1]
        while j > 0 and s[i] != s[j]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p.append(j)
    return p
 
 
 
s = input()
n = len(s)
 
p = prefix_function(s)
 
possible_middles = set(pi[0:-1])
 
j = n - 1
 
while p[j] not in possible_middles and j > 0:
    j = p[j - 1]
 
    
if p[j] == 0:
    print("Just a legend")
else:
    print(s[0:p[j]])
