# this is a sample instructional pygame project!
# since pygame runs in a desktop environment, it can be difficult to find a way to run it.
# luckily, when you install python it automatically comes with a python IDLE Shell, which allows you to write pygame code!
# in order to do this, just open your shell and click "File" and then "New File"
# then, click command s and choose a location to save your file to

# ok, now we're ready to get started! first, import and initialize pygame
import pygame
pygame.init()

# now, we're going to set up the popup screen that displays when pygame runs.
# we're going to store the width and height in variables so that we can reference them later

screen_w = 640
screen_h = 640

# notice the double set of parenthesis--this is because we are passing in a tuple! 
screen = pygame.display.set_mode((screen_w, screen_h))

# now we're going to set the window name for our popup
pygame.display.set_caption("Intro to Pygame Tutorial")

# now, we're going to set up the game loop! this loop contains all of the foundational logic for our game
running = True
while running:
    for event in pygame.event.get():
        # this allows the user to close the popup window when they click the X in the corner
        if event.type == pygame.QUIT:
            running = False

    # setting the screen to white (black by default)
    screen.fill((255, 255, 255))
    
    # updating the display
    pygame.display.flip()

# without this line, clicking the X on pygame would end the loop, but the window would never quit! 
pygame.quit()

# now that you have all of this, test running your game! then, edit the screen fill color and run again. 
