#The answer of leetcode top 1nterview 150 the question number 13 (roman to integer) written by Kasra Namiranian.

class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            "I":        1,
            "V":        5,
            "X":        10,
            "L":        50,
            "C":        100,
            "D":        500,
            "M":        1000,
            "IV":       4,
            "IX":       9,
            "XL":       40,
            "XC":       90,
            "CD":       400,
            "CM":       900
        }

        answer = 0
        i = 0
        while(i<len(s)):
            if s[i:i+2] in conversion:
                answer += conversion[s[i:i+2]]
                i += 2
            else:
                answer += conversion[s[i]]
                i += 1
        return answer

