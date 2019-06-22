class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        def bi_search() -> int:
            nonlocal left
            nonlocal right

            if left == right:
                return left
            else:
                mid = (left + right) // 2
                if isBadVersion(mid):
                    right = mid
                    return bi_search()
                else:
                    left = mid + 1
                    return bi_search()
        
        return bi_search()

def isBadVersion(n):
    if n >= 3:
        return True
    else:
        return False


if __name__ == "__main__":
    solu = Solution()
    print(solu.firstBadVersion(5))