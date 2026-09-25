from pygame import Rect

lane1 = 90
lane2 = 280 
lane3 = 460

class Car:
    car_rect:Rect
    car_color:str
    
    def __init__(self,car_rect,car_color):
        self.car_rect = car_rect
        self.car_color = car_color
