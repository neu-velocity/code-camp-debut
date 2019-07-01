from copy import deepcopy

class Solution:
    def permute(self, nums: list) -> list:
        length = len(nums)
        if length <= 1:
            return [nums]
        elif length == 2:
            return [nums, list(reversed(nums))]
        else:
            inserted_num = nums[0]
            sub_permutations = self.permute(nums[1:])
            permutations = []
            for s_p in sub_permutations:
                for ind in range(len(s_p) + 1):
                    s_p_copy = deepcopy(s_p)
                    s_p_copy.insert(ind, inserted_num)
                    permutations.append(s_p_copy)
            
            return permutations


    def permute_backtrack(self, nums: list) -> list:
        # nested recursive helper function
        def _permute_backtrack(nums: list, cur: list, ans: list) -> None:
            """
            nums: a list of unique numbers
            cur: current partial answer (a list of numbers)
            ans: a list of answers
            """
            if len(cur) == len(nums):
                ans.append(deepcopy(cur))
                return

            for num in nums:
                if num not in cur:
                    cur.append(num)
                    _permute_backtrack(nums, cur, ans)

                    # go backward
                    cur.pop()
        
            return
        

        cur = []
        ans = []
        _permute_backtrack(nums, cur, ans)
        return ans



if __name__ == "__main__":
    solu = Solution()
    print(solu.permute_backtrack([1, 2, 3]))
