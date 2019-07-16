        """
        The time complexity of adding an element in a heap is O(log(k)) 
        and we do it N times that means O(Nlog(k))         
        time complexity for this step.
        """
        d = collections.Counter(nums)
        d = sorted(d.items(), key = lambda x:x[1], reverse = True)
        res = []
        for j in range(k):
            res.append(d[j][0])
        
        return res