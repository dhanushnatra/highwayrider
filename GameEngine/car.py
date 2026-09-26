from pygame import Rect,image,transform
from random import randint
from GameEngine.models import Car,lane1,lane2,lane3
from pathlib import Path
import os

traffic_cars_path = Path("carArt/traffiic_cars")
player_car_path = Path("carArt/player.bmp")

car_size = (100,150)


def create_traffic_car(lane)->Car:
    traffic_car_img = image.load(traffic_cars_path / f"traffic_{randint(1,3)}.bmp" ).convert_alpha()
    traffic_car_img = transform.scale(traffic_car_img,car_size)
    
    car_rect = traffic_car_img.get_rect()
    car_rect.center = (lane,0)
    
    return Car(car_rect,traffic_car_img)

def create_player_car()->Car:
    player_img = image.load(str(player_car_path)).convert_alpha()
    player_img = transform.scale(player_img,car_size)
    
    player_rect = player_img.get_rect()
    player_rect.center = (lane2,850)
    
    return Car(player_rect,player_img)
    


all_lanes = set([1,2,3])



def get_empty_lane(traffic_cars:list[Car])->int:
    full_lanes = set()
    
    for traffic_car in traffic_cars:
        if traffic_car.car_rect.y > 400:
            full_lanes.add(get_player_lane(traffic_car.car_rect))
            
    empty_lanes = all_lanes.difference(full_lanes)
    
    return list(empty_lanes)[0] if len(empty_lanes)==1 else 2

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
                traffic_car = create_traffic_car(lane1)
            case 2:
                traffic_car = create_traffic_car(lane2)
            case 3:
                traffic_car = create_traffic_car(lane3)
        traffic_cars.append(traffic_car)
    return traffic_cars



def move_traffic_cars(traffic_cars:list[Car]):
    for traffic_car in traffic_cars:
        if traffic_car.car_rect.y > 1010:
            traffic_cars.remove(traffic_car)
        if traffic_car.car_rect.y > 400:
            traffic_car.car_color = "yellow"
        traffic_car.car_rect.y+=10
        


def is_colliding(player_car:Car,traffic_cars:list[Car])->bool:
    for traffic_car in traffic_cars:
        if player_car.car_rect.colliderect(traffic_car.car_rect):
            return True
    return False


def get_player_lane(player_rect:Rect)->int:
    player_x = player_rect.x
    if player_x < 120:
        return 1
    else:
        if player_x < 420:
            return 2
        else:
            return 3

speed = 30

def move_player_car_by_y(Y:int,player_car:Car):
    match Y:
        case 0:
            if player_car.car_rect.x <80:
                return
            player_car.car_rect.x -= speed
        case 1:
            pass
        case 2:
            if player_car.car_rect.x > 450:
                return
            player_car.car_rect.x +=speed
            