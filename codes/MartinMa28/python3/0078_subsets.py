from copy import deepcopy

class Solution:
    def subsets(self, nums: list) -> list:
        def combination_backtrack(nums: list, cur: set, ans: list) -> None:
            for num in nums:
                if num not in cur:
                    if len(cur) == 0 or num > cur[-1]:
                        cur.append(num)
                        ans.append(deepcopy(cur))
                        combination_backtrack(nums, cur, ans)
                        cur.pop()
        
        cur = []
        ans = [[]]
        combination_backtrack(nums, cur, ans)
        return ans
                


if __name__ == "__main__":
    solu = Solution()
    print(solu.subsets([1, 2, 3]))
                

