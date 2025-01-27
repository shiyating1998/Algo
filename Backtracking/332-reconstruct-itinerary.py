class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        m = {}
        for item in tickets:
            if m[item[0]]:
                #TODO create a mapping between departure and possible destinations

        

        return h(tickets,"JFK")

class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = ["JFK"]
        used = [0] * len(tickets)

        def h(tickets, start):
            if len(result) == len(tickets) + 1 :
                return result
            
            departList = []

            for i in range(len(tickets)):
                departure, arrival = tickets[i]
                if departure == start and used[i] == 0:
                    departList.append([i,arrival])
            
            departList = sorted(departList, key=lambda x: x[1])  
            #print(departList)
            for i in range(len(departList)):
                if i!=0 and departList[i][1]==departList[i-1][1]:
                    continue
                #print(item)
                result.append(departList[i][1])
                used[departList[i][0]] = 1
                r = h(tickets, departList[i][1])
                if r:
                    return result
                result.pop()
                used[departList[i][0]] = 0

        

        return h(tickets,"JFK")