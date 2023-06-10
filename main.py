import pygame 
import os
from sys import exit

#TODO: implement horizontal and vertical collision for player with platform 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cube Runner")

background_surface = pygame.image.load(os.path.join("OneDrive","Desktop","cube_runner","graphics", "background.png")).convert()
background_surface_smaller = pygame.transform.scale(background_surface,(SCREEN_WIDTH, SCREEN_HEIGHT))

ground_surface = pygame.image.load(os.path.join("OneDrive","Desktop","cube_runner","graphics", "ground.png")).convert()
ground_surface_bigger = pygame.transform.scale(ground_surface, (SCREEN_WIDTH, 100))
ground_rect = ground_surface_bigger.get_rect()

platform_surface = pygame.image.load(os.path.join("OneDrive","Desktop","cube_runner","graphics", "platform.png")).convert_alpha()
platform_rect = platform_surface.get_rect(center = (650,450))

level_01 = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        alive = pygame.image.load(os.path.join("OneDrive","Desktop","cube_runner","graphics", "player.png")).convert()
        dead = pygame.image.load(os.path.join("OneDrive","Desktop","cube_runner","graphics", "player_dead.png")).convert()
        self.state = [alive, dead]
        self.index = 0 

        self.image = self.state[self.index]
        self.rect = self.image.get_rect(midbottom = (50, 550))
        self.gravity = 0
        self.fall_value = 0
    
    def platform_collision(self):
        #print(platform_rect.bottom, platform_rect.top)
        if self.rect.left < 725 and self.rect.right > 575:
            #print(self.rect.bottom, platform_rect.top)
            if self.rect.bottom <= 425:
                #print(self.fall_value)
                self.rect.bottom = platform_rect.top
            if self.rect.top >= 475:
                #print("under platform")
                pass

    def increase_fall_value(self):
        #print(self.fall_value)
        if self.rect.bottom < 550:
            self.fall_value = 3
        if self.rect.bottom == 550: 
           self.fall_value = 0
        if self.rect.left < 725 and self.rect.right > 575:
            if self.rect.bottom >= platform_rect.top:
                self.fall_value = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_SPACE] and self.fall_value <= 2 or keys[pygame.K_UP] and self.fall_value <= 2:
            self.gravity = -20

    def border(self):
        if self.rect.right >= 800:
            self.rect.right = 800
        if self.rect.left <= 0:
            self.rect.left = 0

        

    def fall(self):
        print(self.gravity)
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
        if self.rect.left < 725 and self.rect.right > 575:
            if self.rect.bottom <= 420:
                self.rect.bottom = 425
                self.gravity = -20
    
    def update(self):
        self.platform_collision()
        self.border()
        self.increase_fall_value()
        self.fall()
        self.movement()


player = pygame.sprite.GroupSingle()
player.add(Player())

def draw_window():
    screen.blit(background_surface_smaller,(0,0))
    screen.blit(ground_surface_bigger,(0,550), ground_rect)
    screen.blit(platform_surface, platform_rect)
    player.draw(screen)
    player.update()


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if level_01:
        draw_window()
        pygame.display.update()
        clock.tick(120)