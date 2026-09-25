import torch
from GameEngine.models import Car


def init_traffic_array(traffic_cars:list[Car],player_car:Car):
    traffic_arr = torch.zeros(768,1024)
    for traffic_car in traffic_cars:
        traffic_arr[traffic_car.car_rect.x][traffic_car.car_rect.y] = 1
        # print("traffic car at ",traffic_car.car_rect.x,traffic_car.car_rect.y)
    
    traffic_arr[player_car.car_rect.x][player_car.car_rect.y] = 2
    
    return traffic_arr

def get_traffic_difference(previous_traffic:torch.Tensor,present_traffic:torch.Tensor):
    return (present_traffic-previous_traffic).flatten()