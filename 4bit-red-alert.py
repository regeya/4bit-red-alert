#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = 960, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RED ALERT!!!")

image = pygame.image.load("/home/shane/Documents/tandy-red-alert.png")

cgac = [
    (0, 0, 0),        # Black
    (0, 0, 170),      # Blue
    (0, 170, 0),      # Green
    (0, 170, 170),    # Cyan
    (170, 0, 0),      # Red
    (170, 0, 170),    # Magenta
    (170, 85, 0),     # Brown
    (170, 170, 170),  # Light Gray
    (85, 85, 85),     # Dark Gray
    (85, 85, 255),    # Light Blue
    (85, 255, 85),    # Light Green
    (85, 255, 255),   # Light Cyan
    (255, 85, 85),    # Light Red
    (255, 85, 255),   # Light Magenta
    (255, 255, 85),   # Yellow
    (255, 255, 255),  # White
]

colornums = {}
for i in range(len(cgac)):
    colornums[cgac[i]] = i

colors_to_replace = list(range(3,15,1))

replacement_colors = [8, 4, 6, 12, 14] + [0] * 7

def draw_red_alert(mybasecolors, colors_to_replace, replacement_colors, cgac, colornums, image):
    new_image = image.copy()
    for x in range(new_image.get_width()):
        for y in range(new_image.get_height()):
            pixel_color = new_image.get_at((x, y))
            pixel_color = pixel_color[:3]
            for i in range(len(mybasecolors)):
                print(i)
                replace_color=cgac[mybasecolors[i]]
                replacement_color=cgac[replacement_colors[i]]
                if pixel_color == replace_color:
                    new_image.set_at((x, y), replacement_color)
                    break
    scale_factor = 3
    scaled_image = pygame.transform.smoothscale(new_image, (new_image.get_width() * scale_factor, new_image.get_height() * scale_factor))
    return scaled_image

clock = pygame.time.Clock()
n = 0

running = True
while running:
    n = (n + 1) % 12
    if n > 6:
        mybasecolors = [12, 4] + replacement_colors
    else:
        mybasecolors = [4, 4] + replacement_colors
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    scaled_image = draw_red_alert(mybasecolors, colors_to_replace, replacement_colors, cgac, colornums, image)
    # Draw the scaled image onto the screen
    screen.blit(scaled_image, (0, 0))
    pygame.display.flip()
    clock.tick(5)
    replacement_colors = replacement_colors[-1:] + replacement_colors[:-1]

pygame.quit()