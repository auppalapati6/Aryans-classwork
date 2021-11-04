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

# -- Manages how fast screen refreshes 
clock = pygame.time.Clock()
ball_width = 20
circle_x_pos = 40
x_val = 150
y_val = 200
y_direction = 1
x_direction = 1
x_padd = 0
y_padd = 20

### -- Game Loop 
while not done: 
 # -- User input and controls
 for event in pygame.event.get(): 
  if event.type == pygame.QUIT: 
   done = True 
 for event in pygame.event.get():
   if event.type == pygame.Quit:
     done = True
    #end if
   if event.type == pygame.KEYDOWN:
     if event.type == pygame.KEYUP:
       y_padd = y_padd + 10
   elif event.key == pygame.KEYDOWN:
     y_padd = y_padd-10
     #end if
  #End If
 #Next event
 # -- Game logic goes after this comment
 if x_val == 0 and y_val == y_padd:
   x_direction = x_direction - (2*x_direction) and y_direction = y_direction - (2*y_direction)
 elif x_val < 0 or y_val < 0:
   x_val = 10 and y_val = 10
#endif
 x_val = x_val + x_direction
 y_val = y_val + y_direction
 if y_val > 440 or y_val < 40: 
   y_direction = y_direction * -1 and x_direction = x_direction*-1
 elif x_val > 600 or x_val < 40: 
   y_direction = y_direction * -1 and x_direction = x_direction * -1
 if circle_x_pos > 680:
  circle_x_pos = 40
 else: 
   circle_x_pos = circle_x_pos + 1 
   if keys[pygame.K_UP]:
     y_padd = y_padd - 5
   if keys[pygame.K_DOWN]:
     y_padd = y_padd + 5
   # -- Screen background is BLACK 
   screen.fill (BLACK) 
   # -- Draw here 
   pygame.draw.rect(screen, BLUE, (x_val,y_val,20,20)) 
   # -- flip display to reveal new position of objects 

   pygame.draw.rect(screen, BLUE, (x_padd,y_padd,20,40))  
   pygame.display.flip()
   # - The clock ticks over 
   clock.tick(60) 
   #End While - End of game loop 
pygame.quit()

