class Solution:
    # 最长无重复子串
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] > 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 0:
                if lookup[s[start]] > 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
    # 最小覆盖子串
    def minWindows(self,s:'str',t:'str')-> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0 
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if(lookup[s[end]]) > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end -start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res
    
    # 至多包含两个不同字符的最长字串
    def lengthOfLongerSubstringTwoDistinct(self,s:str)-> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0 
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if(lookup[s[end]]) == 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > 2:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
    
    def getlongestsubstring(self, s):
        hashtable = {}
        max_len = left = 0
        for i, cur_str in enumerate(s):
            if len(hashtable) < 3:
                hashtable[cur_str] = i   
            if len(hashtable) == 3:  
                index = sorted(hashtable.values())[0]  # 在哈希表里的最小索引，left移动，将这个字符移出窗口
                left = index + 1
                hashtable.pop(s[index])  # 移出哈希表
            max_len = max(max_len, i-left+1)
        return max_len
instance = Solution()

if __name__ == '__main__':
    # print(instance.lengthOfLongestSubstring("aabbcd"))
    print(instance.minWindows("adfdcafa","cf"))
    # print(instance.lengthOfLongerSubstringTwoDistinct("adsaaaa"))