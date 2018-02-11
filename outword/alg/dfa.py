#!/usr/bin python
# -*- coding:utf-8 -*-

class DFA(object):
    _root = dict()

    def init_tree(self,wordlist):
        if wordlist:
            for word in wordlist:
                self.add_word(word)

    def add_word(self,word):
        root = self._root
        for char in word:
            if char not in root:
                root[char] = dict()
            root = root.get(char)
        root['end'] = None

    def filter(self,prestr):
        if prestr:
            prestr = list(prestr)
            i = 0
            while i<len(prestr):
                start = i
                end = self.search_tree(start,prestr)
                if start==end:
                    i += 1
                else:
                    prestr[start:end] = '*'*(end-start)
                    i = end
            return ''.join(prestr)

    def search_tree(self,start,prestr):
        root = self._root
        end = temp = start

        while root.get(prestr[temp]):
            root = root.get(prestr[temp])
            temp += 1
            if 'end' in root:
                end = temp
                break
        return end

if __name__ == '__main__':
    siwords = [
        '法轮功',
        '法轮大法',
        '中国共产党',
        '中共',
        '上海帮',
        '日本AV'
    ]
    prestr = '法日本AV我们知道法轮功是反中共的有力武器'

    print(prestr)
    dfa = DFA()
    dfa.init_tree(siwords)
    rst = dfa.filter(prestr)
    print(rst)