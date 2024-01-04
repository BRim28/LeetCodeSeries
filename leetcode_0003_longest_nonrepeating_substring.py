# Leetcode 
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Problem Number: 3
# Date: 2024/01/4

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Approach 1
        '''    
        if len(s)<1:
            return 0
        i = 0
        visited = s[i:i+1]
        max_length = 1
        current = 0
        while True:
            for j in range(i+1,len(s)):
                current = j
                if s[j] in visited:
                    i+=1
                    visited = s[i:i+1]
                    break
                visited = s[i:j+1]
                if len(visited)>max_length:
                    max_length = len(visited)
            if current==len(s)-1:
                break
        return max_length
        '''
        start = max_length = 0
        visited = {} 
        for current,char in enumerate(s):
            if s[current] in visited.keys():
                if visited[s[current]]>=start:
                    start = visited[s[current]]+1
            visited[s[current]] = current
            max_length = max(max_length,current-start+1)
        return max_length
