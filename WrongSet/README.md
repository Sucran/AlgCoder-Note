# 
## Python 基础理解
- `range(start, end, step)`, 生成序列的第一个值是start, 最后一个值是end， 间隔是step
- `list`的`pop`方法和`remove`方法不适合在循环list时一起使用，在前一个元素删掉后，后一个元素就进位，导致循环跳过该元素
- `set(list)`和`list(set)`，list和set可以互相转换，in_place的修改可以使用切片 `list[:] = xx` 来实现
- `list[i:i]` 返回的是 `[ ]`
- `if`和`elif`只会跳入一个分支
- `for`循环从大到小，`for i in range(10, n-1, 0): print i #[10, 9, ..., n]`
- 判断输入为空列表时，直接用`if x == []`



