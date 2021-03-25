# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:11:04 2021

@author: caear
"""
import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=''):
        self.name = newname
    def __str__(self):
        return (f'animal: {str(self.name)}: {str(self.age)}')
    
    
class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return f'cat: {str(self.name)}: {str(self.age)}'
    
    
class Rabbit(Animal):
    def speak(self):
        print('meep')
    def __str__(self):
        return f'rabbit: {str(self.name)}: {str(self.age)}'
    
    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.frineds.append(fname)
    def speak(self):
        print('hello')
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(f'{self.name} is {diff} years older than {other.name}')
        else:
            print(f'{self.name} is {diff} years younger than {other.name}')
    def __str__(self):
        return f'person: {str(self.name)}: {str(self.age)}'
    
    
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print('I am watching tv')
    def __str__(self):
        return f'student: {str(self.name)}: {str(self.age)}: {str(self.major)}'
        