import random

class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(8,10), speed_range=(-1,2)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.speed_range = speed_range

    def motion(self):
        self.motion_x = random.randrange(self.speed_range[0],self.speed_range[1])
        self.motion_y = random.randrange(self.speed_range[0],self.speed_range[1])
        self.x += self.motion_x
        self.y += self.motion_y

    def check_bounds(self):
        if self.x < 0:  self.x = 0
        elif self.x > self.x_boundary:  self.x = self.x_boundary

        if self.y < 0:  self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary