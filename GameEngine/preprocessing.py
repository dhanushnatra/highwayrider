import torch
from GameEngine.models import Car

def preprocess(traffic_cars:list[Car],player_car:Car)->torch.Tensor:
    traffic_arr = torch.zeros(5,2)
    i=0
    for traffic_car in traffic_cars:
        traffic_arr[i][0] = traffic_car.car_rect.x
        traffic_arr[i][1] = traffic_car.car_rect.y
        i+=1
    
    traffic_arr[-1][0] = player_car.car_rect.x
    traffic_arr[-1][1] = player_car.car_rect.y
            
    return traffic_arr.flatten()


def get_y(player_lane:int,empty_lane:int)->torch.Tensor:
    zeros = torch.zeros(3,1)
    if player_lane > empty_lane:
        zeros[0] = 1
    elif player_lane < empty_lane:
        zeros[2] = 1
    else :
        zeros[1] = 1
    return zeros.flatten()
        