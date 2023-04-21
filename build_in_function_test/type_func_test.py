# -*- coding: utf-8 -*-
"""
    :author: allen lv
"""
# Number, 数字
nums1 = 1
nums2 = 1.2
nums3 = 1.23e9

print('{},{},{}'.format(type(nums1), type(nums2), type(nums3)))

# 字符串,String
str1 = ''
str2 = 'str2'
str3 = """今晚夜色真好啊,It's a lovely night
希望明天天气也不错啊,I hope it will be fine tomorrow, too
希望后天天气也不错啊,I hope the weather will be nice the day after tomorrow
"""

print('{},{},{}'.format(type(str1), type(str2), type(str3)))

# 布尔值， Bool
print('{},{}'.format(type(True), type(False)))

# None

print(type(None))

# list

list1 = [1, 2, 3]
list2 = []
list3 = list([1, 2, 3])
print('{0},{1},{2}'.format(type(list1), type(list2), type(list3)))
