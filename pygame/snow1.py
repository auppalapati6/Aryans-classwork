import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
class Snow:
     def __init__(self):
         self.x = 100
         self.y = 0
         self.color = WHITE
         self.height = 30
         self.width = 30
    #end procedure
#end class
def draw(self):
    pygame.draw.rect(screen, WHITE, [self.pos, self.pos, 20, 30])
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
snow1_pos = 0
temp = 0
snow1_pos = 150
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    if y_pos > 470 :
        y_pos = 0
snow1 = Snow()



    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
screen.fill(BLACK)
 
    # --- Drawing code should go here
pygame.draw.rect(screen, WHITE, [x_pos, y_pos, 20, 30])
y_pos = y_pos +1
    # --- Go ahead and update the screen with what we've drawn.
pygame.display.flip()
    
    # --- Limit to 60 frames per second
clock.tick(60)
 
# Close the window and quit.
pygame.quit()               