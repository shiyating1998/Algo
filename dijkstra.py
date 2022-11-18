

# Algo for dijkstra

# find the shortest(weighted) path from start Node to other nodes of the graph

from heapq import heappop,heappush

graph = [[1,5,6],[2,4,5],[3,5,6],[4,7],[],[3,8]]

start = 1 

pq = []
cost = [inf]*len(graph)

heappush(pq, (0, start))

while pq:
    dist, cur_node = heappop(pq)

    if dist>dist[cur_node]:
        continue

    for node in graph[cur]:
        if dist + weight(cur_node,node) <= cost[node]:
            heappush(pq(dist+cost[cur_node], node))
            cost[node] = dist + cost[cur_node]

print(cost) 

# Q1: https://leetcode.cn/problems/path-with-maximum-probability/