class Solution:
    def findKthLargest(self, nums, k) -> int:

        def quick_pos(begin, end):
            pivot = nums[begin]
            while begin < end:
                while end > begin and nums[end] >= pivot:
                    end -= 1
                nums[begin] = nums[end]
                while begin < end and nums[begin] < pivot:
                    begin += 1
                nums[end] = nums[begin]
            nums[begin] = pivot
            return begin

        k = len(nums) - k
        left = 0
        right = len(nums) - 1
        while True:
            piv = quick_pos(left, right)
            if k == piv:
                return nums[piv]
            elif k < piv:
                right = piv - 1
            else:
                left = piv + 1


if __name__ == '__main__':
    a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    s = Solution()
    target = s.findKthLargest(a, 4)
    print(target)
