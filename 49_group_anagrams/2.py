class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dic:
                dic.get(key).append(str)
            else:
                dic[key] = [str]
        return dic.values()

    def run(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        cvp = self.groupAnagrams(strs)
        print(cvp)

if __name__ == "__main__":
    sol = Solution()
    sol.run()
