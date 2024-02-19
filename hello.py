from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    # 最长无重复子串
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
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
    # 至多包含K个不同字符的最长字串
    def lengthOfLongerSubstringKdistinct(self,s:str,k:int)->int:
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
            while counter > k:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
    #找到字符串中的所有字母异位词

    #串联所有单词的字串
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res
    # 滑动窗口
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num :
                    res.append(left)
        return res

    def findSubstring3(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res

    # 一维数组动态和
    def dynamicSum(self,nums:List[int])->List[int]:
        res=[]
        if not nums:
            return res
        n = len(nums)
        res.insert(0,nums[0])
        for i in range(1,n):
            res.insert(i,res[i-1] + nums[i]) 
        return res
    
    # 跳跃游戏 动态规划dp + 双端队列（单调栈）
    def maxResult(self, nums:List[int],k:int)->int:
        n = len(nums)
        dp = [0] *n
        dp[0] = nums[0]
        queue =deque([0])
        for i in range(1,n):
            while queue[0] < i-k:
                queue.popleft()
            dp[i] = nums[i] + dp[queue[0]]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            queue.append(i)
        return dp[n-1]
    
    #跳跃游戏 最小跳跃数
    def jump(self,nums:List[int])->int:
        n = len(nums)
        maxPos = 0
        end = 0
        ans = 0
        for i in range(n-1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                ans += 1
        return ans 
    
instance = Solution()



if __name__ == '__main__':
    # print(instance.lengthOfLongestSubstring("aabbcd"))
    s = "ababaab"
    words = ["ab","ba","ba"]
    nums = [10,-5,-2,4,0,3]
    k = 3
    # print(instance.findSubstring3(s,words))
    # print(instance.dynamicSum(nums))
    # print(instance.lengthOfLongerSubstringTwoDistinct("adsaaaa"))
    print(instance.maxResult(nums,k))
