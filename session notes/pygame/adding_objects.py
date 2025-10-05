# let's start out by copying all of our code from before
import pygame

pygame.init()


screen_w = 640
screen_h = 640

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Intro to Pygame Tutorial")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    rect_w = screen_w - 20
    rect_h = 50

    # 1. now, let's add some shapes! we can use this using pygame.draw.shape_name
    # the third parameter is a tuple in the format (x, y, width, height)
    pygame.draw.rect(screen, (0, 0, 0), ((screen_w/2) - (rect_w/2), (screen_h) - (rect_h), rect_w, rect_h))
    
    pygame.display.flip()

pygame.quit()
