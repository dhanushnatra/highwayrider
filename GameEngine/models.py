from pygame import Rect
from io import BytesIO

start = 5
lane1 = 130 + start
lane2 = 240 + start
lane3 = 390 + start

car_lane1 = (start+lane1) / 2
car_lane2 = (lane1+lane2) / 2
car_lane3 = (lane2+lane3) / 2

class Car:
    car_rect:Rect
    car_image:BytesIO
    
    def __init__(self,car_rect,car_image):
        self.car_rect = car_rect
        self.car_image = car_image
