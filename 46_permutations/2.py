class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return [[]]
        res = []
        for i in range(n):
            for p in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + p)
        return res

    def run(self):
        nums = [1,2,3]
        cvp = self.permute(nums)
        print(cvp)

if __name__ == "__main__":
    sol = Solution()
    sol.run()
