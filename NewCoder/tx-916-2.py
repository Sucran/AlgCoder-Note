#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
import math
line = sys.stdin.readline().strip()
a = line.split()
x = int(a[0])
y = int(a[1])
sum_s = x + y
n = int(round(math.sqrt(sum_s * 2)))
temp_x = x
count = 0
for i in range(n, 0, -1):
    if temp_x >= i:
        temp_x -= i
        count += 1
        if temp_x == 0:
            break
print count
