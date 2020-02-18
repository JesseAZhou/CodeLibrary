""" find all possible ways to break the sentence in individual dictionary words"""
# 输出句子匹配字典中单词的所有可能性
# 如果用户自定义字典,则只匹配自定义字典中的单词
# 如果用户自定义字典， 则找出匹配两个字典的单词所有可能性

from collections import deque


class InputSelection:
    def __init__(self):
        self.word_set = {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'man go'}
        self.only_customized = '2'
        self.both_dict = '3'
        self.origin_str = 'ilikesamsungmobile'

    def update_set(self, input_str):
        if input_str:
            input_set = set(input_str.split(','))
            select_stage = input("input 2 only use customized dictionary, 3 will find words in both dictionaries:")
            if select_stage == self.only_customized:
                return input_set
            elif select_stage == self.both_dict:
                input_set.update(self.word_set)
                return input_set
        else:
            return self.word_set

    def update_string(self, input_str):
        return self.origin_str if not input_str else input_str


class Solution:
    def word_break(self, long_str, word_set):
        size = len(long_str)

        dp = [False for _ in range(size)]
        dp[0] = long_str[0] in word_set

        for right_s in range(1, size):
            if long_str[:right_s + 1] in word_set:
                dp[right_s] = True
                continue

            for left_s in range(right_s):
                if dp[left_s] and long_str[left_s + 1: right_s + 1] in word_set:
                    dp[right_s] = True
                    break
        res = []
        if dp[-1]:
            queue = deque()
            self.__dfs(long_str, size - 1, word_set, res, queue, dp)
        return res

    def __dfs(self, long_str, end, word_set, res, que, dp):
        if long_str[:end + 1] in word_set:
            que.appendleft(long_str[:end + 1])
            res.append(' '.join(que))
            que.popleft()

        for i in range(end):
            if dp[i]:
                suffix = long_str[i + 1:end + 1]
                if suffix in word_set:
                    que.appendleft(suffix)
                    self.__dfs(long_str, i, word_set, res, que, dp)
                    que.popleft()


if __name__ == '__main__':
    # new_str = 'ilikesamsungmobile'
    # new_set = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'man go']
    in_str = input('input a sentence or click "ENTER" to skip:')
    in_set = input('input customized dictionary or click "ENTER" to skip (E.g.:cat,dog,pig,cow):')
    solution = Solution()
    input_select = InputSelection()
    new_str = input_select.update_string(input_str=in_str)
    new_set = input_select.update_set(input_str=in_set)
    result = solution.word_break(new_str, new_set)
    print(result)
