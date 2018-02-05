#!/usr/bin/env python3
#coding:utf-8



class Dog(object):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name.lower().capitalize()
    def set_name(self,value):
        self._name = value
    def bark(self):
        print(self.get_name() + ' is making sound wang wang wang...')

class Cat(object):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name.lower().capitalize()
    def set_name(self,value):
        self._name = value
    def mew(self):
        print(self.get_name() + ' is making sound miu miu miu...')

dog = Dog('wangcai')

cat = Cat('Kitty')

dog.bark()
cat.mew()        
