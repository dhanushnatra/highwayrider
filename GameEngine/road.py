from pygame.draw import line
from GameEngine.models import lane1,lane2,lane3,start

def draw_road(screen):
    line(screen,"white",(lane1,1024),(lane1,0),2)
    line(screen,"white",(lane2,1024),(lane2,0),2)
    line(screen,"white",(lane3,1024),(lane3,0),2)
    line(screen,"white",(start,1024),(start,0),2)
    
def draw_threshold(screen):
    line(screen,"grey",(0,400),(600,400),2)
    line(screen,"grey",(0,500),(600,500),2)