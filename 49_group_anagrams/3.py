class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

    def run(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        cvp = self.groupAnagrams(strs)
        print(cvp)

if __name__ == "__main__":
    sol = Solution()
    sol.run()
