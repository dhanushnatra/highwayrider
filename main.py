
import pygame
from GameEngine.road import draw_road
from GameEngine.car import spawn_traffic,move_traffic_cars,create_car,lane2,is_colliding,move_player_car_by_y,get_player_lane
from torch import Tensor
from GameEngine.preprocessing import preprocess,get_y
from model_setup import convert_to_int,save_model,load_model
from Brain.rl_model import model_loop

pygame.init()


w1,b1,w2,b2,w3,b3 = load_model()

screen = pygame.display.set_mode((640,1024))
pygame.display.set_caption("highway rider")

clock = pygame.time.Clock()
running = True


tick_count = 0
player_car = create_car(lane2,"green",is_player=True)

traffic = spawn_traffic()
traffic_cars = traffic[0]
empty_lane = traffic[1]
actual_y = get_y(get_player_lane(player_car.car_rect),empty_lane)
print("empty lane =",empty_lane)
print("player lane = ",get_player_lane(player_car.car_rect))
learning_rate:float = 0.01

# speed = 20

# def move_player_car(player:pygame.Rect,keys):

#     if keys[pygame.K_LEFT] or keys[pygame.K_a]:
#         player.x -= speed

#     if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
#         player.x += speed

#     if keys[pygame.K_UP] or keys[pygame.K_w]:
#         player.y -= speed

#     if keys[pygame.K_DOWN] or keys[pygame.K_s]:
#         player.y += speed


try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        if tick_count!=0:
            
            if tick_count==36:
                empty_lane = traffic[1]
                actual_y = get_y(get_player_lane(player_car.car_rect),empty_lane)
                print("empty lane =",empty_lane)
                print("player lane = ",get_player_lane(player_car.car_rect))
            
            if tick_count==60:
                tick_count=0
                traffic = spawn_traffic()
                traffic_cars+=traffic[0]
        
        
        x = preprocess(traffic_cars,player_car)
        
        w1,b1,w2,b2,w3,b3,y_hat = model_loop(w1,b1,w2,b2,w3,b3,x,actual_y,learning_rate)
        
        move_player_car_by_y(convert_to_int(y_hat),player_car)

        screen.fill("#313131")
        draw_road(screen)
        
        move_traffic_cars(traffic_cars)

        for traffic_car in traffic_cars:
            pygame.draw.rect(screen,traffic_car.car_color,traffic_car.car_rect)
        
        
        pygame.draw.rect(screen,player_car.car_color,player_car.car_rect)
        
        keys = pygame.key.get_pressed()
        # move_player_car(player_car.car_rect,keys)
        
        
        
        
        
        
        if is_colliding(player_car,traffic_cars):
            player_car.car_rect.y = 850
            traffic_cars = []
            del traffic
            tick_count=0
            traffic = spawn_traffic()
            traffic_cars+=traffic[0]
            
        
        
        pygame.display.flip()
        clock.tick(20)
        tick_count+=1
        
    pygame.quit()

except KeyboardInterrupt:
    save_model(w1,b1,w2,b2,w3,b3)