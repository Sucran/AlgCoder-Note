## 算法题-面试题-做题笔记 Algorithm-Interview-Coding-Note

## 经典问题
- 判断素数
    - 如果一个数i是素数，那么xrange(i*i, n, i)都不是素数
    - 0和1不是素数, 2是素数，3也是素数
    - 判断素数和求n以内的素数个数 LeetCode`[204]`

- 最大子列和
    - 在线处理 LeetCode`[53]`
        - LeetCode`[121][122]` 最大两点差值（前一点减去后一点）
    - 分治法

- 判断链表中是否存在环
    - 快慢指针方法 LeetCode`[141]`

## 基础数据结构

### 链表
```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```





