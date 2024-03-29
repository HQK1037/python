from typing import List
from collections import defaultdict
from collections import deque

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
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
    
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1,n):
            if nums[i-1] < nums[i]:
                dec = False
            if nums[i-1] > nums[i]:
                inc = False
        return dec or inc
    
    #单调递增数字
    def monotoneIncreasingDigits(self, n: int) -> int:
        ans = n
        arr = list(str(n))
        max = -1
        idx = -1 
        for i in range(len(arr)-1):
            if max < int(arr[i]):
                max = int(arr[i])
                idx = i
            if arr[i] > arr[i+1]:
                arr[idx] = str(int(arr[idx]) - 1)
                for j in range(idx + 1,len(arr)):
                    arr[j] = '9'
        return int(''.join(arr))
    
    #重排链表
    def reorderList(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return
        # 找中间节点
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 反转
        pre,cur =None, slow.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node

        #合并链表
        p1,p2 = head,pre
        while p2:
            tmp1,tmp2 = p1.next,p2.next
            p1.next = p2
            p2.next = tmp1
            p1,p2 = tmp1,tmp2
    def creatList(self,nums):
        if not nums:
            return None
        
        head = ListNode(nums[0])
        cur = head
        for num in nums[1:]:
            cur.next = ListNode(num)
            cur = cur.next
        return head
    def printList(self,head):
        cur = head
        while cur:
            print(cur.val,end = " ")
            cur = cur.next
        print()

    # BFS: 队列  DFS：栈
    def canReachBFS(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        n = len(arr)
        used = {start}
        q = deque([start])

        while len(q) > 0:
            u = q.popleft()
            for v in [u + arr[u], u - arr[u]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    q.append(v)
                    used.add(v)
        
        return False
    
    def canReachDFS(self, arr: List[int], start: int) -> bool:
        def DFS(arr:List[int],start:int,visited:deque[bool]):
            if start < 0 or start >= len(arr) or visited[start]:
                return False
            if arr[start] == 0:
                return True
            visited[start] = True
            return DFS(arr,start-arr[start],visited) or DFS(arr,start+arr[start],visited)
        n = len(arr)
        visited = deque(n*[False])
        return DFS(arr,start,visited)



instance = Solution()



if __name__ == '__main__':
    # print(instance.lengthOfLongestSubstring("aabbcd"))
    s = "ababaab"
    words = ["ab","ba","ba"]
    nums = [1,2,3,4,5]
    arr = [4,2,3,0,3,1,2]
    start = 5
    # num = 1234
    # k = 3
    # print(instance.findSubstring3(s,words))
    # print(instance.dynamicSum(nums))
    # print(instance.lengthOfLongerSubstringTwoDistinct("adsaaaa"))
    # print(instance.maxResult(nums,k))
    # print(instance.monotoneIncreasingDigits(10))
    # head =instance.creatList(nums)
    # instance.reorderList(head)
    # instance.printList(head)
    print(instance.canReachDFS(arr,start))