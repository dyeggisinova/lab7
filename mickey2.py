import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((830, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("MickeyClock")

mickey = pygame.image.load("clock.png")

minutes = pygame.image.load("min_hand.png")
seconds = pygame.image.load("sec_hand.png")

center_x, center_y = 400, 300

running = True
while running:
    screen.blit(mickey, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    angle1 = -minute * 6  # Rotate correctly for minutes
    angle2 = -second * 6  # Rotate correctly for seconds

    rot_min = pygame.transform.rotate(minutes, angle1)
    rot_sec = pygame.transform.rotate(seconds, angle2)

    min_rect = rot_min.get_rect(center=(center_x, center_y))
    sec_rect = rot_sec.get_rect(center=(center_x, center_y))

    screen.blit(rot_min, min_rect)
    screen.blit(rot_sec, sec_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
