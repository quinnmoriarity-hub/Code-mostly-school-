
# Example file showing a basic pygame "game loop"
import pygame
import random
import math
class Boid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((8,8))
        self.points = [
            pygame.Vector2(0,1),
            pygame.Vector2(0,1),
            pygame.Vector2(0,1)
        ]
        
        
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()

        self.fov = 75
        self.dir = pygame.Vector2(random.random() *2 -1 ,random.random() *2 -1).normalize()
        
        print(self.dir)
        self.speed = .3


    def draw_triangle(self, angle: float, size: int, image: pygame.Surface ):
        image.fill("black")
        image.set_colorkey("black")
        offset = pygame.Vector2(image.get_width()/2, image.get_width()/2)
        points = [
            pygame.Vector2(0,-size).rotate(angle) + offset, 
            pygame.Vector2(0,-size).rotate(angle).rotate(135) + offset,
            pygame.Vector2(0,-size).rotate(angle).rotate(225) + offset

        ]
        pygame.draw.polygon(image, "white", points)

    def update(self, dt):
        self.rect.move_ip(self.dir *self.speed*dt)
        if self.rect.x > 1280: # This allows for boids to pull a pack man :)
            self.rect.x = 0 
        if self.rect.y > 720:
            self.rect.y = 0
        if self.rect.x < 0:
            self.rect.x = 1280
        if self.rect.y < 0:
            self.rect.y = 720
        #this code will allow the boids to social distance
         

        for b in self.groups()[0]: #check all boids
            if pygame.Vector2( pygame.Vector2(self.rect.center) -  pygame.Vector2(b.rect.center)).length() > 40: # is a boid in our radius
                angle2boid = self.dir.angle_to( pygame.Vector2(self.rect.center) -  pygame.Vector2(b.rect.center))
                if abs(angle2boid) < self.fov: # is it in our line of sight
                    # turn
                    if angle2boid > 0:
                        self.dir.rotate_ip(5)
                        for p in self.points:
                            p.rotate_ip(5)
                    elif angle2boid == 0: 
                        self.dir.rotate_ip(-5)
                        for p in self.points:
                            p.rotate_ip(-5)
                    else:
                        self.dir.rotate_ip(-5)
                        for p in self.points:
                            p.rotate_ip(-5)
        
#DRAW THE TRIANGLE
        self.draw_triangle(self.dir.angle_to(pygame.Vector2(0,1)), 4, self.image)




# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0



boil= pygame.sprite.Group()

for i in range (20):
    b = Boid()
    boil.add(b)
    b.rect.center = (300,200)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    boil.update(dt)

    boil.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60)  # limits FPS to 60

pygame.quit()