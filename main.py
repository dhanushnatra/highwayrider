
import pygame
from GameEngine.road import draw_road
from GameEngine.car import spawn_traffic,move_traffic_cars,create_car,lane2,is_colliding,move_player_car_by_y,get_player_lane
from torch import Tensor
from GameEngine.preprocessing import preprocess
from model_setup import predict


pygame.init()

screen = pygame.display.set_mode((640,1024))
pygame.display.set_caption("highway rider")

clock = pygame.time.Clock()
running = True


tick_count = 0
player_car = create_car(lane2,"green",is_player=True)

traffic = spawn_traffic()
traffic_cars = traffic[0]
empty_lane = traffic[1]
print("empty lane =",empty_lane)
print("player lane = ",get_player_lane(player_car.car_rect))


speed = 20

def move_player_car(player:pygame.Rect,keys):

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    if tick_count!=0:
        
        if tick_count==30:
            empty_lane = traffic[1]
            print("empty lane =",empty_lane)
            print("player lane = ",get_player_lane(player_car.car_rect))
        
        if tick_count==60:
            tick_count=0
            traffic = spawn_traffic()
            traffic_cars+=traffic[0]
    
    move_player_car_by_y(predict(preprocess(traffic_cars,player_car)),player_car)
    
            

    screen.fill("#313131")
    draw_road(screen)
    
    move_traffic_cars(traffic_cars)

    for traffic_car in traffic_cars:
        pygame.draw.rect(screen,traffic_car.car_color,traffic_car.car_rect)
    
    
    pygame.draw.rect(screen,player_car.car_color,player_car.car_rect)
    
    keys = pygame.key.get_pressed()
    move_player_car(player_car.car_rect,keys)
    
    if is_colliding(player_car,traffic_cars):
        print("cars collided")
        break
    
    
    pygame.display.flip()
    clock.tick(20)
    tick_count+=1
    
pygame.quit()