class Circle:
    def __init__(self, radius):
        self.radius = radius
        if radius < 0:
            raise ValueError('radius must be positive')

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            raise ValueError('radius must be positive')
        else:
            self._radius = new_radius

    @property    
    def diameter(self):
        diameter = 2 * self._radius
        return diameter

    @property
    def circumference(self):
        circumference = 2 * 3.14 * self._radius
        return circumference

    def area(self):
        area = 3.14 * self._radius * self._radius
        return area
