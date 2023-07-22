# -*- coding: utf-8 -*-
"""
    :author: allen lv
    @property
"""

# 对学生的score进行限制

class Student:

    def get_score(self):
        return self._score

    def set_score(self, newscore):
        if not isinstance(newscore, int):
            raise ValueError('score must be integer')
        elif newscore < 0 or newscore > 100:
            raise ValueError('score must between 0 ~ 100')
        else:
            self._score = newscore


s = Student()
s.set_score(88)
print(s.get_score())
# s.set_score(10000)  # 数字太大会报错


# 下面是使用@property改进
class Student1():

    # getter的方法名 score
    # @property getter
    @property
    def score(self):
        return self._score

    # setter的方法名score
    # @score.setter 是 setter
    @score.setter
    def score(self, newscore):
        if not isinstance(newscore, int):
            raise ValueError('score must be integer')
        elif newscore < 0 or newscore > 100:
            raise ValueError('score must between 0 ~ 100')
        else:
            self._score = newscore

s1 = Student1()
s1.score = 60
print(s1.score)
# s1.score = 1000  # 数字太大会报错


# 只读属性
"""
class Student:
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def age(self):
        return 2015- self.birth
"""

"""
class Student:
    
    @property
    def birth(self):
        return self.birth
"""


"""
# 测试
class Screen:

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_wid):
        self._width = new_wid

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_hei):
        self._height = new_hei


    @property
    def resolution(self):
        return self._height * self._width
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
"""
