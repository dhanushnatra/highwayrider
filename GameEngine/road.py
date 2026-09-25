from pygame.draw import line

def draw_road(screen):
    line(screen,"white",(220,1024),(220,0),2)
    line(screen,"white",(420,1024),(420,0),2)
    line(screen,"white",(600,1024),(600,0),2)
    line(screen,"white",(40,1024),(40,0),2)
    
def draw_threshold(screen):
    line(screen,"grey",(0,400),(768,400),2)
    line(screen,"grey",(0,500),(768,500),2)