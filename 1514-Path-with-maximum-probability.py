
# 1514 Path with maximum probability: https://leetcode.cn/problems/path-with-maximum-probability/
from heapq import heappush,heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = [[] for _ in range(n)]     

        for i in range(len(edges)):
            f = edges[i][0]
            t = edges[i][1]
            graph[f].append((t,succProb[i]))
            graph[t].append((f,succProb[i]))

        pq = []
        heappush(pq, (-1,start))
        probs = [-inf]*n

        while pq:
            cur_prob, node = heappop(pq)
            cur_prob = -cur_prob

            if node==end:
                return cur_prob
            
            if cur_prob < probs[node]:
                continue

            for new_node, weight in graph[node]:
                new_prob = weight*cur_prob
                if new_prob > probs[new_node]:
                    heappush(pq, (-new_prob, new_node))
                    probs[new_node] = new_prob
        
        return 0
           


# Algo for dijkstra

# find the shortest(weighted) path from start Node to other nodes of the graph

# from heapq import heappop,heappush

# graph = [[1,5,6],[2,4,5],[3,5,6],[4,7],[],[3,8]]

# start = 1 

# pq = []
# cost = [inf]*len(graph)

# heappush(pq, (0, start))

# while pq:
#     dist, cur_node = heappop(pq)

#     if dist>dist[cur_node]:
#         continue

#     for node in graph[cur]:
#         if dist + weight(cur_node,node) <= cost[node]:
#             heappush(pq(dist+cost[cur_node], node))
#             cost[node] = dist + cost[cur_node]

# print(cost) 
 