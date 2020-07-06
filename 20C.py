import sys
from heapq import *
 
inf = int(1e12)
n, m = map(int, input().split())
 
parent = [-1]*n
dis = [inf]*n
graph = [[] for i in range(n)]
dis[0] = 0
for i in range(m):
	a,b,c = map(int, input().split())
	graph[a-1].append((b-1,c))
	graph[b-1].append((a-1,c))
 
q = [(0, 0)]
while q:
	w, node = heappop(q)
	for nodes in graph[node]:
		if dis[nodes[0]] > dis[node]+nodes[1]:
			dis[nodes[0]] = dis[node]+nodes[1]
			parent[nodes[0]] = node
			heappush(q, (dis[nodes[0]], nodes[0]))
 
if parent[n-1] == -1:
	print(-1)
else:
	path = []
	s = n-1
	while s != -1:
		path.append(s+1)
		s = parent[s]
	path.reverse()
	print(*path)