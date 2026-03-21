class Solution:
    def longestPalindrome(self, s: str) -> str:
      #expand around center technique
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

        max_palindrome=""

        for i in range(len(s)):
            p1=expand(i,i) #odd length
            p2=expand(i,i+1) #even length
            if len(p1)>len(max_palindrome):
                max_palindrome=p1
            if len(p2)>len(max_palindrome):
                max_palindrome=p2

        return max_palindrome
            
            
        
        
