# agani, let's start by copying our code from the last session
import pygame

pygame.init()


screen_w = 640
screen_h = 640

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Adding Sprites")
# now, we know that we can add shapes. but what if we don't want to draw out
# something ourselves? well, we can import images

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # let's add a sprite to represent our player
    # first, we need to download the image
    # you can check out some assets at https://kenney.nl/assets/category:2D
    
    
    # I will be using these https://kenney.nl/assets/pixel-platformer-food-expansion
    # to add some blocks
    block_img = pygame.image.load("C:\\Users\\dawoo\\Downloads\\kenney_pixel-platformer-food-expansion\\Tiles\\tile_0103.png")

    dimensions = block_img.get_rect()
    dimensions.topleft = (0,0)

    screen.blit(block_img, dimensions)
    
    pygame.display.flip()

pygame.quit()
