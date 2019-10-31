"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function. 
"""
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        res = 0
        num = 0
        sign = 1
        stk = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                res *= stk.pop()
                res += stk.pop()
                num = 0
                sign = 1

        if num:
            res += sign * num
        return res