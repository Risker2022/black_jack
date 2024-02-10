import pygame

from .button import Button
from ..functions import draw_text

class text_area(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(255, 255, 255), starting_text="", font=pygame.font.match_font("sans-serif"), font_color=(0, 0, 0), outline=((0, 0, 0), 1)):
        # Init the parent class
        pygame.sprite.Sprite.__init__(self)

        # Create the image
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Postition text area
        self.rect.x = x
        self.rect.y = y
        
        # Set the outline
        self.outline = outline
        pygame.draw.rect(self.image, self.outline[0], pygame.Rect(0, 0, self.rect.width, self.rect.height), self.outline[1])

        # Store the font
        self.font = font
        self.font_color = font_color

        # store starting text
        self.text = starting_text

        # Draw the staring text
        draw_text(self.image, 0, 2, self.text, size=self.rect.height - 2, font=self.font, color=self.font_color)

        # Selected state
        self.selected = False

        # Store the color
        self.color = color

        # Shifted keys
        self.shifted_keys = {
            pygame.K_1: "!",
            pygame.K_2: "@",
            pygame.K_3: "#",
            pygame.K_4: "$",
            pygame.K_5: "%",
            pygame.K_6: "^",
            pygame.K_7: "&",
            pygame.K_8: "*",
            pygame.K_9: "(",
            pygame.K_0: ")",
            pygame.K_BACKQUOTE: "~",
            pygame.K_MINUS: "_",
            pygame.K_EQUALS: "+",
            pygame.K_LEFTBRACKET: "{",
            pygame.K_RIGHTBRACKET: "}",
            pygame.K_BACKSLASH: "|",
            pygame.K_SEMICOLON: ":",
            pygame.K_QUOTE: "\"",
            pygame.K_COMMA: "<",
            pygame.K_PERIOD: ">",
            pygame.K_SLASH: "?",
        }
    
    def update(self):
        # Check if the text area is selected
        self.check_select()

        # Redraw the white rect
        self.image.fill(self.color)

        # Draw the outline
        pygame.draw.rect(self.image, self.outline[0], pygame.Rect(0, 0, self.rect.width, self.rect.height), self.outline[1])

        # Draw the text
        draw_text(self.image, self.rect.width / 2, 4, self.text, size=self.rect.height - 2, font=self.font, color=self.font_color)


    def check_select(self):
        click_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if click_state[0] == True:
            if self.rect.collidepoint(mouse_pos):
                self.selected = True
                print("Selected")
            else:
                self.selected = False

    def typed_key(self, key):
        if self.selected:
            # Check if shift is pressed
            shift_pressed = pygame.key.get_mods() & pygame.KMOD_SHIFT

            # Check if the key is a number key
            if pygame.K_SPACE <= key <= pygame.K_z:
                # Check if it is shifted
                if shift_pressed:
                    # Deal with special characters
                    if key in self.shifted_keys:
                        self.text="".join([self.text, self.shifted_keys[key]])
                        print(key)

                    # Deal with capital letters
                    elif pygame.K_a <= key <= pygame.K_z:
                        self.text="".join([self.text, chr(key).upper()])
                        print(key)
                
                # Check if it is not shifted
                else:
                    self.text="".join([self.text, chr(key)])
                    print(key)

            elif key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                print("Backspace")
    
    def get_value(self):
        return self.text
