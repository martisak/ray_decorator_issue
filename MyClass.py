import ray


@ray.remote
class MyClass(object):

    """ This is my decorated class """

    def __init__(self, a):
        """
        The constructor

        :param a: The a parameter
        :type a: int
        """

        self.a = a


class MyUndecoratedClass(object):

    """ This is my undecorated class """

    def __init__(self, a):
        """
        The constructor

        :param a: The a parameter
        :type a: int
        """

        self.a = a

    def get_a(self):
        """
        :returns: the a
        """

        return self.a


if __name__ == "__main__":

    ray.init()

    c1 = MyClass.remote(0)
    c2 = MyUndecoratedClass(0)

