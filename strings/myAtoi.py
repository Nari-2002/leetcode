class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:       
            return 0

        sign = 1
        r = ""
        i = 0

        
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            i = 1


        for ch in s[i:]:
            if ch.isdigit():
                r += ch
            else:
                break

        if r == "":      
            return 0

        num = sign * int(r)

        
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num
