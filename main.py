
import pygame
from GameEngine.road import draw_road,draw_threshold
from GameEngine.car import spawn_traffic,move_traffic_cars,create_player_car,is_colliding,move_player_car_by_y,get_player_lane,get_empty_lane
from GameEngine.preprocessing import preprocess,get_y
from model_setup import convert_to_int,save_model,load_model
from Brain.rl_model import model_loop
from Brain.model_parts import cross_entropy

pygame.init()


w1,b1,w2,b2,w3,b3 = load_model()

screen = pygame.display.set_mode((640,1024))
pygame.display.set_caption("highway rider")

clock = pygame.time.Clock()
running = True


tick_count = 0
player_car = create_player_car()

traffic_cars = spawn_traffic()
learning_rate:float = 0.001

mistakes = 0

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
        
        player_lane = get_player_lane(player_car.car_rect)
        empty_lane = get_empty_lane(traffic_cars)
        # print("player lane=",player_lane)
        # print("empty lane=",empty_lane)
        
        actual_y = get_y(player_lane,empty_lane)
        
        if tick_count!=0:
            
            if tick_count==60:
                tick_count=0
                traffic_cars += spawn_traffic()
                print("Cost =",cross_entropy(y_hat,actual_y))
        
        x = preprocess(traffic_cars,player_car)
        
        
        w1,b1,w2,b2,w3,b3,y_hat = model_loop(w1,b1,w2,b2,w3,b3,x,actual_y,learning_rate)
        
        move_player_car_by_y(convert_to_int(y_hat),player_car)

        screen.fill("#313131")
        draw_road(screen)
        draw_threshold(screen)
        
        move_traffic_cars(traffic_cars)

        for traffic_car in traffic_cars:
            screen.blit(traffic_car.car_image,traffic_car.car_rect)
        
        
        screen.blit(player_car.car_image,player_car.car_rect)
        
        keys = pygame.key.get_pressed()
        # move_player_car(player_car.car_rect,keys)
        
        
        
        if is_colliding(player_car,traffic_cars):
            player_car.car_rect.y = 850
            traffic_cars = []
            tick_count=0
            traffic_cars = spawn_traffic()
            player_car.car_rect.x = 300
            player_car.car_rect.y = 800
            mistakes+=1
            
        
        
        pygame.display.flip()
        clock.tick(20)
        tick_count+=1
        
    pygame.quit()

except KeyboardInterrupt:
    save_model(w1,b1,w2,b2,w3,b3)
    print("total mistakes made =",mistakes)