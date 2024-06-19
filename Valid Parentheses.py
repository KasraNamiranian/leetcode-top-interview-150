#The answer of leetcode top 1nterview 150 the question number 20 valid parentheses written by Kasra Namiranian.

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif not stack:
                return False
            elif i==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif i=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif i==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
    
solution=Solution()
s="()"  #True
a=solution.isValid(s)
print(a)

s="()[]{}"  #True
a=solution.isValid(s)
print(a)

s="(]"  #False
a=solution.isValid(s)
print(a)
