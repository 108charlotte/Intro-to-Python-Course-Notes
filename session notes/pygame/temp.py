import pygame

pygame.init()


screen_w = 640
screen_h = 640

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Adding Sprites")
character = pygame.image.load("C:\\Users\\dawoo\\Downloads\\kenney_pixel-platformer-food-expansion\\Tiles\\tile_0103.png")
dimensions = character.get_rect()

block_h = dimensions.height

# see bottom of game loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(character, dimensions)
        
    screen.fill((255, 255, 255))
    
    pygame.display.flip()
    
    clock.tick(60)


pygame.quit()
