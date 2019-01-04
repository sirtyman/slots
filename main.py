import timeit


""" Present advantage and drawbacks of using classes with and without __slots__ defined 
    Note: This example use Python 3.x (f-strings and print function)
"""


class WithoutSlots(object):

    """Definition of class without __slots__"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithSlots(object):

    """Definition of class with __slots__"""

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


setup = 'import main'
withoutSlotsInst = WithoutSlots('x', 'y')
withSlotsInst = WithSlots('x', 'y')


def create_instances_benchmark(num=1000000):
    print('Assign values to attributes to instance of class w/o slots')
    t = timeit.timeit('main.withoutSlotsInst.x = "x"; '
                      'main.withoutSlotsInst.y = "y"',
                      setup, number=num)
    print(t)

    print('Assign values to attributes to instance of class w/ slots')
    t = timeit.timeit('main.withSlotsInst.x = "x"; '
                      'main.withSlotsInst.y = "y"',
                      setup, number=num)
    print(t)


def assignment_benchmark(num=1000000):

    """ Measures time of assignments to attributes of instance of class w/o __slots__ and w/ __slots__"""

    print('Assign values to attributes of instance w/o slots')
    t = timeit.timeit('main.WithoutSlots("x", "y")', setup, number=num)
    print(t)

    print('Create instances with slots time')
    t = timeit.timeit('main.WithSlots("x", "y")', setup, number=num)
    print(t)


if __name__ == '__main__':

    print('Adding attribute dynamically to instance of WithoutSlots is allowed')
    withoutSlotsInst.z = 'z'
    print(f'Printing withoutSlotsInst.__dict__: {withoutSlotsInst.__dict__}')

    print('Adding attribute y dynamically to instance of WithSlots is prohibited. See exception:')
    try:
        withSlotsInst.z = 'z'
    except AttributeError as e:
        print(e.args)

    print(f'withSlotsInst has no attribute __dict__')
    try:
        print(f'Printing withoutSlotsInst.__dict__: {withSlotsInst.__dict__}')
    except AttributeError as e:
        print(e.args)

    create_instances_benchmark(num=100000000)  # 100 millions times
    assignment_benchmark(num=100000000)  # 100 million times
