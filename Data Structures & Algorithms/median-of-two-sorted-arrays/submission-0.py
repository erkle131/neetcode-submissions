class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        L, R = 0, len(A)
        while L <= R:
            i = (L + R) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")
            Bleft = B[j - 1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")

            # partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                R = i - 1
            else:
                L = i + 1