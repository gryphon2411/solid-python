# ISP: The Interface Segregation Principle

# (2017)

# (2002)

# (2000) Many client specific interfaces are better than one
# general purpose interface

# Simplified: No client should be forced to depend on methods it does
# not use


class Shape:
    def area(self):
        raise NotImplemented

    def volume(self):
        raise NotImplemented


class Circle(Shape):
    def area(self):
        """code for drawing a circle"""
        pass

    def volume(self):
        """empty implementation. Circle do not have volume"""
        pass


class Cube (Shape):
    def area(self):
        """code for drawing a circle"""
        pass

    def volume(self):
        """code for drawing square"""
        pass
