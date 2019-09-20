import queue
import copy
import time


class Solution:
    def get_dict(self, text: str):
        d = {k: 0 for k in text}
        for each in text:
            d[each] += 1
        return d

    def maxNumberOfBalloons(self, text: str) -> int:
        d1 = self.get_dict(text)
        d2 = self.get_dict('balloon')
        rst = len(text) // 7
        for k, v in d2.items():
            if k not in d1:
                return 0
            rst = min(rst, d1[k] // v)
        return rst

def main():
    test = 'nlaebolko'
    rst = Solution()
    print(rst.maxNumberOfBalloons(test))

if __name__ == '__main__':
    main()