class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            print(key)

    def run(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        self.groupAnagrams(strs)

if __name__ == "__main__":
    sol = Solution()
    sol.run()
