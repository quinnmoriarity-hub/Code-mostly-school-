import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

image = pygame.Surface((40,40))
 
def draw_triangle(angle: float, size: int, image: pygame.Surface ):
    image.fill("black")
    image.set_colorkey("black")
    offset = pygame.Vector2(image.get_width()/2, image.get_width()/2)
    points = [
        pygame.Vector2(0,-size).rotate(angle) + offset, 
        pygame.Vector2(0,-size).rotate(angle).rotate(135) + offset,
        pygame.Vector2(0,-size).rotate(angle).rotate(225) + offset

    ]
    pygame.draw.polygon(image, "white", points)

    





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    draw_triangle(45,15,image)
    screen.blit(image, (100,100))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

# Example file showing a circle moving on screen


    


    

pygame.quit()