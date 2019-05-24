class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = 0
        while t < n:
            t += 1
            nums1[m + t - 1] = nums2.pop()

        nums1.sort()
        return None
