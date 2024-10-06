
class Solution(object):
    def isValid(self, s):
        b = []
        for j in s:
            if j in "({[":
                b.append(j)
            else:
                if not b or (j == ")" and b[-1] != "(") or (j == "}" and b[-1] != "{") or (j == "]" and b[-1] != "["):
                    return False                 
                b.pop()
        return not b

        
        
        