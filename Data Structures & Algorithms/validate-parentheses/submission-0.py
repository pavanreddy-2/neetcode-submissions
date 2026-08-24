class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid ={'(':')','{':'}','[':']'}
        for ch in s:
            if ch == '(' or  ch == '{' or ch =='[':
                stack.append(ch)
            elif len(stack) > 0 and ((ch==')' and stack[-1]=='(') or (ch==']' and stack[-1]=='[') or (ch=='}' and stack[-1]=='{')):
                stack.pop()
            else:
                stack.append(ch)
        if len(stack)==0:
            return True
        else:
            return False