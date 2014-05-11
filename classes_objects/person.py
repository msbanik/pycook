"""
   Created by mbani002 on 5/10/14.
"""


class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        print "first_name's getter is called"
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        print "first_name's setter is called"
        if not isinstance(value, str):
            raise ValueError('String required')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (1 < value < 100):
            raise ValueError('Invalid value for age')
        self._age = value

    @age.deleter
    def age(self):
        raise AttributeError('age cannot be deleted')

    def get_gender(self):
        return self._gender
    def set_gender(self, gender):
        if gender not in ('M', 'F', 'B'):
            raise ValueError('gender code is not correct')
        self._gender = gender
    gender = property(get_gender, set_gender)

    def phone():
        doc = "The phone number property."
        def fget(self):
            return self._phone
        def fset(self, value):
            self._phone = value
        def fdel(self):
            del self._phone
        return locals()
    phone = property(**phone())

if __name__ == '__main__':
    p = Person('Rony')
    p.first_name = 'R'
    p.age = 20
    p.gender = 'M'
    p.phone = '7868006741'
    # del p.first_name