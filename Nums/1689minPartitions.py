class Solution:
    def minPartitions(self, n: str) -> int:
        m=0
        for i in n:
            if(m<int(i)):
                m=int(i)
        return m
