import pygame

from os import path

def draw_text(surface, x, y, text, size=20, font=pygame.font.match_font("sans-serif"), color=(0, 0, 0)):
    font=pygame.font.Font(font, size)
    text_surface=font.render(text, True, color)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x, y)
    surface.blit(text_surface, text_rect)

def draw_image(surface, image, x, y):
    surface.blit(image, (x, y))

def get_dir(name):
    return path.join(path.dirname(__file__), name)

def get_image(img_dir, name):
    return pygame.image.load(path.join(img_dir, name)).convert_alpha()

def transform_image(image, width, height):
    return pygame.transform.scale(image, (width, height))
    