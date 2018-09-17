import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
line3 = sys.stdin.readline().strip()
k = int(line1)
str_a = line2
str_b = line3

sub_str_set = set()
count = 0
for i in range(len(str_a)):
   sub_str = str_a[i:i+k]
   if len(sub_str) == k:
       if sub_str not in sub_str_set:
           sub_str_set.add(sub_str)
           if str_b.find(sub_str) != -1:
               count += 1

print count