#Calculate Sphere volume, area and density

import math

class Sphere(object):
	# Good Luck!
    def __init__(self,radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        self.volume = (4/3)*math.pi*self.radius**3
        return round(self.volume,5)
        
    def get_surface_area(self):
        self.area=4*math.pi*self.radius**2
        return round(self.area,5)
        
    def get_density(self):
        self.density = self.mass / self.volume
        return round(self.density,5)
    

ball = Sphere(2,50)

# test.assert_equals(ball.get_radius(),2, "Check radius")
# test.assert_equals(ball.get_mass(),50, "Check mass")
# test.assert_equals(ball.get_volume(), 33.51032, "Check volume")
# test.assert_equals(ball.get_surface_area(),50.26548, "Check area")
# test.assert_equals(ball.get_density(),1.49208, "Check density")