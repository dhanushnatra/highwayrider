from pygame import Rect
from io import BytesIO

lane1 = 100
lane2 = 300 
lane3 = 480

class Car:
    car_rect:Rect
    car_image:BytesIO
    
    def __init__(self,car_rect,car_image):
        self.car_rect = car_rect
        self.car_image = car_image
