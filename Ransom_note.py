The answer of leetcode top 1nterview 150 the question number 383 (ransom note) written by Kasra Namiranian.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
