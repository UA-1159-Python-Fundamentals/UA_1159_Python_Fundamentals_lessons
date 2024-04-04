from math import pi
class Sphere(object):
    def __init__(self, r, m):
        self.r = r
        self.m = m
        
    def get_radius(self):
        return self.r
    
    def get_mass(self):
        return self.m
    
    def get_volume(self):
        return 4 * pi * self.r**3 / 3
    
    def get_surface_area(self):
        return 4 * pi * self.r**2
    
    def get_density(self):
        area = 4 * pi * self.r**3 / 3
        return self.m / area
