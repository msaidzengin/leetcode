import collections
class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for st in strs:
            s = ''.join(sorted(st))
            dic[s].append(st)

        return dic.values()

    def run(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        cvp = self.groupAnagrams(strs)
        print(cvp)

if __name__ == "__main__":
    sol = Solution()
    sol.run()
