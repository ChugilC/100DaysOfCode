import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Actual window
pygame.display.set_caption("Space Game")


WHITE = (255, 255, 255)

FPS = 60

YELLOW_SPACESHIP = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
RED_SPACESHIP = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))

def draw_window():
        WIN.fill(WHITE) # Change the color
        WIN.blit(YELLOW_SPACESHIP)

        pygame.display.update() # Update the screen 


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            # Handling quit event
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()