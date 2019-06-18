class Solution:
    def topKFrequent(self, nums:list, k:int) -> list:
        element_counter = {}
        for n in nums:
            element_counter[n] = element_counter.get(n, 0) + 1
        
        sorted_elements =  sorted(element_counter.items(), key=lambda x: x[1], reverse=True)
        return [e[0] for e in sorted_elements[:k]]