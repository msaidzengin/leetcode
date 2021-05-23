class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start_index = 0
        maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start_index <= usedChar[s[i]]:
                start_index = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start_index + 1)
            usedChar[s[i]] = i


            print(usedChar)
            print(maxLength)

        return maxLength

    def run(self):
        print(self.lengthOfLongestSubstring("abcabcbb"))
    
sol = Solution()
sol.run()
