#!/usr/bin/python
# -*- coding:utf-8 -*-

# 单例模式, __new__方法
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

# 单例模式，装饰器版本
# 此处装饰器修饰的是一个类，_singleton函数接受创建一个类对象的参数
def singleton(cls):
    _instance = {}
    def _singleton(*args, **kwargs):
        print 'in _singleton decorator'
        if not cls in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton

@singleton
class Class_single(object):
    def __init__(self):
        print 'in Class_single __init__'

# 元类模式(这种方法只能在python3环境下有效)
# 定义的类实际是元类生成的对象
class Singleton_Type(type):
    # __call__方法的self参数，指向用户自定义的类，相当于定义了类方法__call__
    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Singleton_Type, self).__call__(*args, **kwargs)
        return self._instance

class Singleton2(object, metaclass=Singleton_Type):
    pass

def try_singleton():
    a = Class_single()
    b = Class_single()
    print 'a is b: %s' % (a is b, )


if __name__ == '__main__':
    try_singleton()
