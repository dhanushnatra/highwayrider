from pygame import Rect
from random import randint

lane1 = 90
lane2 = 280 
lane3 = 460


def spawn_traffic()->list[Rect]:
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
                traffic_car = Rect(lane1,0,100,150)
            case 2:
                traffic_car = Rect(lane2,0,100,150)
            case 3:
                traffic_car = Rect(lane3,0,100,150)
        traffic_cars.append(traffic_car)
    
    print(lanes)    
    return traffic_cars



def move_traffic_cars(traffic_cars:list[Rect]):
    for traffic_car in traffic_cars:
        traffic_car.y+=10