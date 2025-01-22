class Solution:
    def isPalindrome(self, s):
        if len(s) == 1:
            return True 
        
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False 
            start += 1 
            end -= 1
        
        return True 

    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []

        def h (l , s, startIndex):
            if l == len(s):
                result.append(path[:])
                return
            
            for partition in range(startIndex, len(s)):   
                for i in range(partition + 1, len(s) + 1):
                    if self.isPalindrome(s[partition:i]):
                        path.append(s[partition:i])
                        l += i - partition 
                        h(l, s ,i)
                        path.pop()
                        l -= i - partition
        
        h(0, s, 0)
        return result 
            
        