import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class House:
  def __init__(self): 
    self.x = 100
    self.y = 440
    self.colour = RED
    self.height = 100
    self.width = 200
  #end procedure
  def update(self):
    pass

  def draw(self):
    pygame.draw.rect(screen, self.colour, [self.x,self.y,self.height,self.width])
  #end procdure
#end class


## -- Define the class snow which is a sprite 
class player(pygame.sprite.Sprite): 
# Define the constructor for snow 
  def __init__(self, color, width, height): 
  # Call the sprite constructor 
    super().__init__() 
    # Create a sprite and fill it with colour 
    self.image = pygame.Surface([width,height]) 
    self.image.fill(color) 
    # Set the position of the sprite 
    self.rect = self.image.get_rect() 
    self.rect.x = (0, 200) 
    self.rect.y = (0, 100) 
  #End Procedure
  def update(self):
    pass
#End Class


## -- Define the class snow which is a sprite 
class invaders(pygame.sprite.Sprite): 
# Define the constructor for snow 
  def __init__(self, color, width, height): 
  # Call the sprite constructor 
    super().__init__() 
    # Create a sprite and fill it with colour 
    self.image = pygame.Surface([width,height]) 
    self.image.fill(color) 
    # Set the position of the sprite 
    self.rect = self.image.get_rect() 
    self.rect.x = random.randrange(0, 600) 
    self.rect.y = 0-random.randrange(0, 50) 
  #End Procedure
  def update(self):
    if self.rect.y > 500:
      self.rect.x = random.randint(0,700)
      self.rect.y = 0
    else:
      self.rect.y = self.rect.y + 1
#End Class
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
invaders_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
all_sprites_groups = pygame.sprite.Group()
for n in range(12):
  INVADER_PERSON = invaders(GREEN,10,10)
  invaders_group.add(INVADER_PERSON)
  all_sprites_groups.add(INVADER_PERSON)
for n in range(1):
  player = invaders(RED,10,10)
  player_group.add(player)
  all_sprites_groups.add(player)
#next n
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
# --- Game logic should go here
    all_sprites_groups.update()

# --- Screen-clearing code goes here
 
# Here, we clear the screen to white. Don't put other drawing commands
# above this, or they will be erased with this command.
 
# If you want a background image, replace this clear with blit'ing the
# background image.
    screen.fill(BLACK)
 
# --- Drawing code should go here
# snow1.draw()
# snow2.draw()
# snow3.draw()
#for sprite in sprites:
#sprite.draw()
    all_sprites_groups.draw(screen)
# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
