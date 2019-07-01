from copy import deepcopy

class Solution:
    def permutationUnique(self, nums: list) -> list:
        def _permute_backtrack(nums: list, used: list, cur: list, ans: list) -> None:
            """
            nums: a list of integers which could contain duplicates
            used: a list of boolean value indicating if that integer is used
            cur: current partial permutation
            ans: a list of answers (full permutations)
            """
            if len(cur) == len(nums):
                if cur not in ans:
                    ans.append(deepcopy(cur))
                return

            for i, num in enumerate(nums):
                if not used[i]:
                    cur.append(num)
                    used[i] = True
                    _permute_backtrack(nums, used, cur, ans)

                    # go backward
                    cur.pop()
                    used[i] = False
            
            return

        used = [False] * len(nums)
        cur = []
        ans = []

        _permute_backtrack(nums, used, cur, ans)
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.permutationUnique([1, 1, 2]))
                
