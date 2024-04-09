class Sphere(object):

    PI = 3.14159265359
    
    def __init__(self, radius, mass):
        self.r = radius
        self.m = mass
        
    def get_radius(self):
        return self.r
    
    def get_mass(self):
        return self.m
    
    def get_volume(self):
        return round((4*__class__.PI*self.r**3)/3, 5)
    
    def get_surface_area(self):
        return round(4*__class__.PI*self.r**2, 5)
    
    def get_density(self):
        return round(self.m/self.get_volume(), 5)