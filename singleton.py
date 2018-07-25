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

def try_singleton():
    a = Class_single()
    b = Class_single()
    print 'a is b: %s' % (a is b, )


if __name__ == '__main__':
    try_singleton()
