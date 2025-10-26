# agani, let's start by copying our code from the last session
import pygame

pygame.init()


screen_w = 640
screen_h = 640

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Adding Sprites")
block_img = pygame.image.load("C:\\Users\\dawoo\\Downloads\\kenney_pixel-platformer-food-expansion\\Tiles\\tile_0103.png")
dimensions = block_img.get_rect()

block_h = dimensions.height

sushi_positions = []
# keeps track of the velocities of the sushi blocks
sushi_velocities = []

gravity = 0.5

# see bottom of game loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            sushi_positions.append((pos))
            sushi_velocities.append(0)

    screen.fill((255, 255, 255))

    # since I now need to edit the original values in the sushi_positions list,
    # I can no longer use a for-each loop since I need to refer directly back to the values
    # (a for-each loop allows me to look at what the values are but not to modify them in the original list)
    for i in range(len(sushi_positions)):
        # updates the velocites based on gravity (not a realistic physics model)
        sushi_velocities[i] = sushi_velocities[i] + gravity

        # updates sushi positions
        # the first value is the x-value, the 2nd is the y-value
        sushi_positions[i] = (sushi_positions[i][0], sushi_positions[i][1] + sushi_velocities[i])


        # updates sushi velocity when hitting floor
        if sushi_positions[i][1] > screen_h - block_h / 2 and sushi_velocities[i] > 0:
            sushi_velocities[i] *= -0.5
            sushi_positions[i] = (sushi_positions[i][0], screen_h - block_h / 2)
                            
        dimensions.center = sushi_positions[i]
            
        screen.blit(block_img, dimensions)
    
    pygame.display.flip()
    # this will create a delay to make our falling animation more realistic
    clock.tick(60)


pygame.quit()
