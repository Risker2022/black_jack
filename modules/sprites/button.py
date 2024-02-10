import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, text, font=pygame.font.match_font("sans-serif"), font_size=None, font_color=(255, 0, 0), color=(255, 255, 255), outline=((0 ,0 ,0), 1), pos_mod=(0, 0)):
        # Init the parent class
        pygame.sprite.Sprite.__init__(self)

        # Coordinates of button
        self.image = pygame.Surface((width, height))
        # Colour the button
        self.image.fill(color)

        # Position of button
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Draw the outline
        outline_rect = pygame.Rect(0, 0, width, height)
        pygame.draw.rect(self.image, outline[0], outline_rect, outline[1])

        # Text on button
        # Determine the font size
        if not font_size:
            font_size = height

        # Create the text
        font = pygame.font.Font(font, font_size)
        text = font.render(text, True, font_color)
        text_rect = text.get_rect()

        # Determine text position
        text_rect.center = (width / 2, height / 2)     # Blit uses positition relative to surface, not screen

        # Set the position modifier
        self.pos_mod_x, self.pos_mod_y = pos_mod

        # Draw the text
        self.image.blit(text, text_rect)
    
    def is_clicked(self):
        click_state = pygame.mouse.get_pressed()
        if click_state[0] == True:  # Check if the mouse is clicked
            # Check if the mouse is over the button
            mouse_pos = pygame.mouse.get_pos()
            if (((self.rect.x + self.pos_mod_x) <=
                 mouse_pos[0] <=
                 (self.rect.x + self.rect.width + self.pos_mod_x))
                and
                ((self.rect.y + self.pos_mod_y)
                 <= mouse_pos[1] <=
                 (self.rect.y + self.rect.height + self.pos_mod_y))):
                # Returns a True for whether the button has been clicked
                return True
        return False
