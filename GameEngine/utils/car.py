from pygame import Rect,key
from random import randint

lane1 = 90
lane2 = 280 
lane3 = 460

class Car:
    car_rect:Rect
    car_color:str
    
    def __init__(self,car_rect,car_color):
        self.car_rect = car_rect
        self.car_color = car_color



def create_car(lane,color,is_player=False)->Car:
    return Car(Rect(lane,850 if is_player else 0,100,150),color)

def spawn_traffic()->list[Car]:
    traffic_cars = []
    lanes = [randint(1,3)]
    
    while True:
        random_lane = randint(1,3)        
        if random_lane not in lanes:
            lanes.append(random_lane)
            break

    for lane in lanes:
        match lane:
            case 1:
                traffic_car = create_car(lane1,"blue")
            case 2:
                traffic_car = create_car(lane2,"blue")
            case 3:
                traffic_car = create_car(lane3,"blue")
        traffic_cars.append(traffic_car)
    
    print(lanes)    
    return traffic_cars



def move_traffic_cars(traffic_cars:list[Car]):
    for traffic_car in traffic_cars:
        traffic_car.car_rect.y+=10


def is_colliding(player_car:Car,traffic_cars:list[Car])->bool:
    for traffic_car in traffic_cars:
        if player_car.car_rect.colliderect(traffic_car.car_rect):
            return True
    return False