# encoding = utf-8
import heapq
import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        mid = math.ceil((len1 + len2) / 2)
        heap = list()
        index1 = index2 = 0
        while index1 < len1 and index2 < len2:
            if nums1[index1] < nums2[index2]:
                heap.append(nums1[index1])
                index1 += 1
            else:
                heap.append(nums2[index2])
                index2 += 1
        heap += nums1[index1: mid - len(heap) + 1] if index1 < len(nums1) \
            else nums2[index2: mid - len(nums2) + 1]
        return (heap[-1] + heap[-2]) / 2 if (len1 + len2) % 2 == 0 else heap[-1]

    def right_solution(self, nums1, nums2):

        def worker(arr1, arr2):
            len1 = len(arr1)
            len2 = len(arr2)
            start, end = 0, len1
            while start <= end:
                partition_1 = (start + end) // 2
                partition_2 = (len1 + len2 + 1) // 2 - partition_1

                max_left_1 = -math.inf if partition_1 == 0 else arr1[partition_1 - 1]
                min_right_1 = math.inf if partition_1 == len1 else arr1[partition_1]

                max_left_2 = -math.inf if partition_2 == 0 else arr2[partition_2 - 1]
                min_right_2 = math.inf if partition_2 == len2 else arr2[partition_2]

                if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2 \
                        if (len1 + len2) % 2 == 0 else max(max_left_1, max_left_2)
                elif max_left_1 > min_right_2:
                    end = partition_1 - 1
                else:
                    start = partition_1 + 1

        return worker(nums1, nums2) if len(nums1) < len(nums2) else worker(nums2, nums1)

    def test_function(self):
        # case1
        nums1 = [1, 3]
        nums2 = [2]
        print(self.right_solution(nums1, nums2))


if __name__ == '__main__':
    s = Solution()
    s.test_function()
