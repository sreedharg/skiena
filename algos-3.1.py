class Stack(object):
    def __init__(self):
        self.data = []
    
    def push(self, val):
        self.data.append(val)
        
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

class Solution(object):
    def check_if_valid_parenthesis(self, inp):
        my_stack = Stack()

        valid = True

        for i, x in enumerate(inp_str):
            if x == "(":
                my_stack.push(x)
            elif x == ")":
                last_val = my_stack.pop()
                if last_val != "(":
                    valid = False
                    break

        if len(my_stack.data) > 0:
            valid = False
        
        if valid:
            return -1
        else:
            return i
        
inp_str = "((()))()"

sol = Solution()
x = x = sol.check_if_valid_parenthesis(inp_str)
if x == -1:
    print("valid string")
else:
    print("invalid string at ", x)