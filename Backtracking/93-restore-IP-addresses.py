class Solution:

    def validSegment(self, s):
        
        if len(s) == 1:
            return True 

        if s[0] != '0':
            if int(s) <= 255 and int(s) >= 0:
                return True

        return False       

    def restoreIpAddresses(self, s: str) -> List[str]:

        path = []
        result = []
        count = 0 
        

        def h (count, s, startIndex):

            if count == len(s) and len(path) == 4:
                result.append(".".join(path))
                return 

            if startIndex >= len(s):
                return 

            if 4 - len(path) > len(s) - startIndex:
                return 
            
            if 3*(4 - len(path)) < len(s)-startIndex:
                return 
            
            # 1 digit always valid 
            path.append(s[startIndex])
            count += 1 
            h(count, s, startIndex + 1)
            path.pop()
            count -= 1 

            # 2 digits 
            if len(s) > startIndex + 1:
                if self.validSegment(s[startIndex:startIndex+2]):
                    path.append(s[startIndex:startIndex+2])
                    count += 2 
                    h(count, s , startIndex + 2)
                    path.pop()
                    count -= 2 
            
            if len(s) > startIndex + 2:
                if self.validSegment(s[startIndex:startIndex+3]):
                    path.append(s[startIndex:startIndex+3])
                    count += 3 
                    h(count, s , startIndex + 3)
                    path.pop()
                    count -= 3 
        

        h(0,s,0)
        return result 

# Time Complexity: O(3^4), 3 branches and max depth of 4   
#  Space Complexity: O(n) 