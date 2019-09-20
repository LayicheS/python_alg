import queue
import copy
import time

class Solution:
    def rev(self, s, start, end):
        s[start:end+1] = s[end:start-1:-1]

    def reverseParentheses(self, s: str) -> str:
        tmp = list(s)
        bracket = []
        for i,v in enumerate(tmp):
            if v == '(':
                bracket.append(i)
            if v == ')':
                self.rev(tmp, bracket[-1]+1, i-1)
                bracket.pop()
        rst = ''.join(tmp)
        print(rst)
        rst = rst.replace('(', '')
        rst = rst.replace(')', '')
        return rst

def main():
    test = 'a(bcdefghijkl(mno)p)q'
    rst = Solution()
    print(rst.reverseParentheses(test))

if __name__ == '__main__':
    main()