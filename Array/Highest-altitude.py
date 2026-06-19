# https://leetcode.com/problems/find-the-highest-altitude/description/
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r=0
        m=0
        for i in gain:
            r=r+i
            if m<r:
                m=r
        return m
