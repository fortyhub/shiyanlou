#!/usr/bin/env python3

class Animal(object):
    def __init__(self,name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound miu miu miu...')

dog = Dog('wangcai')
cat = Cat('Kitty')
dog.make_sound()
cat.make_sound()
    
