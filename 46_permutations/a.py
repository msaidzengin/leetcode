class Solution:

    def permute(self, nums):
        print(nums)
        return [
            [n] + p for i, n in enumerate(nums) 
            for p in self.permute(nums[:i] + nums[i+1:])
        ] or [[]]

    def run(self):
        nums = [1,2,3]
        cvp = self.permute(nums)
        print(cvp)

if __name__ == "__main__":
    sol = Solution()
    sol.run()

