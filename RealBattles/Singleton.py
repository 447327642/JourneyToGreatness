# Peter Norvig's way of Python Singleton

def singleton(object, instantiated=[]):
    """ Raise an exception if an object of this class has been instantiated 
        before
    """
    print instantiated
    assert object.__class__ not in instantiated, \
        "%s is a Singleton class but is already instantiated" % object.__class__
    instantiated.append(object.__class__)

class Single:
    """ A singleton
    """
    def __init__(self, args):
        singleton(self)
        

a = Single("a")

# b = Single("b")
