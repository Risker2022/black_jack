import pygame

from time import time

from .button import Button
from ..functions import get_image, get_dir, draw_text

class NumberSlider(pygame.sprite.Sprite):
    def __init__(self, surface, x, y, width, height, start=0, end=5, color=(255, 255, 255), outline=((0, 0, 0), 1)):
        # Initiallise the parent class
        pygame.sprite.Sprite.__init__(self)

        # Create the image and rect
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Postition the slider
        self.rect.x = x
        self.rect.y = y

        # Store the start and end values
        self.start = start
        self.end = end
        self.value = self.start

        # Store the color
        self.color = color

        # Set the outline
        self.outline = outline
        pygame.draw.rect(self.image, self.outline[0], pygame.Rect(0, 0, self.rect.width, self.rect.height), self.outline[1])

        # Make variables to control the frequency of button presses
        self.last_press = time()
        self.press_delay = 0.1

        # Store the buttons
        self.button_left = Button(0, 0, height, height, "<", color=(230, 230, 230), font_color=(0, 0, 0), pos_mod=(self.rect.x, self.rect.y))
        self.button_right = Button(width-height, 0, height, height, ">", color=(230, 230, 230), font_color=(0, 0, 0), pos_mod=(self.rect.x, self.rect.y))

    def update(self):
        # Check if the buttons are clicked
        if time() - self.last_press > self.press_delay:
            if self.button_left.is_clicked():
                # Decreases the value by 1
                self.value -= 1

                # Check to see if the value is less than the min value
                if self.value < self.start:
                    self.value = self.start
                
                # Reset the time
                self.last_press = time()
            if self.button_right.is_clicked():
                # Increases the value by 1
                self.value += 1

                # Check to see if the value is greater than the max value
                if self.value > self.end:
                    self.value = self.end

                # Reset the time
                self.last_press = time()
        
        # Clears the previous drawings
        self.image.fill(self.color)

        # Draw the outline
        pygame.draw.rect(self.image, self.outline[0], pygame.Rect(0, 0, self.rect.width, self.rect.height), self.outline[1])

        # Draw the buttons
        self.image.blit(self.button_left.image, (0, 0))
        self.image.blit(self.button_right.image,
                        (self.rect.width - self.button_right.rect.width, 0))

        # Draw the text
        draw_text(self.image,
                  self.rect.width / 2,
                  5,
                  str(self.value),
                  size=self.rect.height, color=(0, 0, 0))
        
    def get_value(self):
        return self.value