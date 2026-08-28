class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in s:
            if i == ']':
                char = ""
                while stack[-1] != '[':
                    char = stack.pop() + char
                stack.pop() # remove '['
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                count = int(num)
                new_str = count * char
                stack.append(new_str)
            else:
                stack.append(i)
        return "".join(stack)