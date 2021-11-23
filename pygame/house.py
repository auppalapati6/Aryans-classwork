import pygame 
# -- Global Constants 

# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 

# -- Initialise PyGame
pygame.init() 

# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 

# -- Title of new window/screen 
pygame.display.set_caption("My Window") 

# -- Exit game flag set to false 
done = False
sun_x = 40
sun_y = 150
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()

### -- Game Loop 
while not done: 
  # -- User input and controls
   for event in pygame.event.get(): 
     if event.type == pygame.QUIT: 
       done = True 

   #End If
   
   #Next event

   # -- Game logic goes after this comment
   temp = 0
   sun_x = sun_x + 5
   if sun_x < 320:
     sun_y = sun_y - 2 
   if sun_x > 320:
       sun_y = sun_y +2
   if sun_x > 639:
       sun_x = 40
       sun_y = 150
   # -- Screen background is BLACK 
   screen.fill (BLACK) 
   # -- Draw here 
   pygame.draw.rect(screen, BLUE, (220,150,200,150)) 
   pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)

   # -- flip display to reveal new position of objects 
   pygame.display.flip()
   # - The clock ticks over 
   clock.tick(60) 
#End While - End of game loop 
pygame.quit()