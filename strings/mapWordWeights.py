class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans = ""

        for word in words:
            total = 0
            for c in word:
                total += weights[ord(c) - ord('a')]

            rem = total % 26
            ans += chr(ord('z') - rem)

        return ans
