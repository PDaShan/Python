# a = input("请输入一个字段：")
# b = input("请输入另一个字段：")
# c = len(a) + len(b)
# print(c)
# print(type(3))
# print(type(True))

# 元组
# s = (1,2.3,3,4,"嘻嘻","嘿嘿","哈哈")
# print(s[6])

# 统计某个值在元组中个数
# print(s.count("哈哈"))

# 查看某个下标位置
# print(s.index("嘻嘻"))

# 元组下标
# a = (s,"嘻嘻","哈哈")
# print(a[1])

# 二维元组
# print(a[0][1])
# print(a[-1])

'''
# 切片
print(s[:3])  # 从什么开始可省略
print(s[3:5])
print(s[5:])  #  从什么结束可省略

'''

# 数组
s = [1,2.3,3,4,"嘻嘻","嘿嘿","哈哈"]
# print(s[6])
# 在数组最后面追加数据
s.append("append1")
print(s)

# 在数组中插入数据
s.insert(3,"芜湖")
print(s)

# 剪切
s.pop(4)
b = s.pop(4)
print(b)

a = s.pop(0)
b = s.pop(0)
print(a + b)
