
import pygame

#big class for stuff
class x:
    invaders = []
    bullets = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False
        
        player = Player(self, width/2, height-20)
        alienmaker = ALIENMAKER(self)
        bullet = None
        while not done:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                player.x -= 2 if player.x > 20 else 0  
            elif pressed[pygame.K_RIGHT]:  
                player.x += 2 if player.x < width - 20 else 0  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.bullets.append(Bullet(self, player.x, player.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for invader in self.invaders:
                invader.draw()
                invader.checkCollision(self)
                if (invader.y > height):
                    self.lost = True
                    

            for bullet in self.bullets:
                bullet.draw()

            if not self.lost: player.draw()

#bad guy
class invader:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 15

    def draw(self):
        pygame.draw.rect(self.game.screen,  
            (100, 255, 100),  
            pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05

    def checkCollision(self, game):
        for bullet in game.bullets:
            if (bullet.x < self.x + self.size and
                    bullet.x > self.x - self.size and
                    bullet.y < self.y + self.size and
                    bullet.y > self.y - self.size):
                game.bullets.remove(bullet)
                game.invaders.remove(self)

#good guy
class Player:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
            (100, 100, 255),
            pygame.Rect(self.x, self.y, 8, 5))


class ALIENMAKER:
    def __init__(self, game):
        margin = 30  
        width = 50  
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.invaders.append(invader(game, x, y))

        


class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen,  
                         (254, 52, 110),  
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2  


if __name__ == '__main__':
    game = x(600, 400)