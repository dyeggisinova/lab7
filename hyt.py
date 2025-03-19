

import pygame

pygame.init()
clock_img = pygame.image.load("clock.png")
width, height = clock_img.get_size()
print("Clock image size:", width, height)
print("Center coordinates:", width // 2, height // 2)
