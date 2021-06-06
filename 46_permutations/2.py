def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
            