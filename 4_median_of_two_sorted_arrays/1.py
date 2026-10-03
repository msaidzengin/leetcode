class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.findKth(A, B, l // 2)
        return (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B, l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        return self.findKth(A[i:], B[:j], j)
