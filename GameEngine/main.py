
import pygame
from utils.road import draw_road
from utils.lanes import spawn_traffic,move_traffic_cars

pygame.init()

screen = pygame.display.set_mode((640,1024))
pygame.display.set_caption("highway rider")

clock = pygame.time.Clock()
running = True


tick_count = 0

traffic_cars = spawn_traffic()

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    # player.update()
    
    if tick_count%60==0 and tick_count!=0:
        traffic_cars += spawn_traffic()
    
    screen.fill("#313131")
    draw_road(screen)
    
    move_traffic_cars(traffic_cars)

    for traffic_car in traffic_cars:
        pygame.draw.rect(screen,"blue",traffic_car)
    # Draw
    # player.draw(screen)

    pygame.display.flip()
    clock.tick(20)
    tick_count+=1
    
pygame.quit()