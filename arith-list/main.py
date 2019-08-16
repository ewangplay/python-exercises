#!/usr/local/bin/python3

from arith_list import ArithmeticSequence

s = ArithmeticSequence(1, 2)
print("forth item: ", s[4])
s[4] = 2
print("changed forth item: ", s[4])
print("fifth item: ", s[5])

# 因为没有实现__delitem__协议接口，所以不能
# 对元素进行删除操作
# del s[4]
