# Pygame template-skeleton for a new pygame project
import pygame
import socket

import random

from modules.sprites import button, text_box, number_slider
from modules import functions


def connect_to_server():
    # Connect to server
    ip = input("Enter the IP address of the server: ")
    port = 9999

    # Create a socket object
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((ip, 9999))
    msg = socket.recv(1024)
    print(msg.decode("utf-8"))

    socket.close()


def main():
    #Define constants
    #Constant for Screen Width, Height and FPS
    WIDTH = 800
    HEIGHT = 600
    FPS = 30

    #Define constant colours
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (255,255,0)

    #Initialise pygame and create window
    pygame.init()

    # Get the images directory
    img_dir = functions.get_dir("images")

    #Enable sound effects in game
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #set the caption of the screen
    pygame.display.set_caption("Black Jack")

    #Set speed of the game
    clock = pygame.time.Clock()
    #A sprite group is just a collection of sprites that you can act on all at the same time
    # Normal Sprite groups
    start_sprites = pygame.sprite.Group()
    request_ip_sprites = pygame.sprite.Group()
    player_selection_sprites = pygame.sprite.Group()

    # Connect to the server
    # connect_to_server()

    # Store images
    images = {
        "start_title": functions.transform_image(functions.get_image(img_dir, "start_title.png"), 700, 400),
        "card_background_1": functions.transform_image(functions.get_image(img_dir, "card_background.png"), WIDTH, 400),
        "card_background_2": functions.transform_image(functions.get_image(img_dir, "card_background.png"), WIDTH, 400),
    }
    print(images["start_title"])

    # Create the sprites

    # Start screen sprites
    create_server_button = button.Button(x=WIDTH / 2 - 300, y=400, width=200, height=50, text="New Game", font_color=BLACK)
    create_client_button = button.Button(x=WIDTH / 2 + 100, y=400, width=200, height=50, text="Join Game", font_color=BLACK)


    # Request ip sprites
    text_area_ip = text_box.text_area(x=WIDTH / 2 - 300, y=300, width=400, height=50)
    comfirm_ip_button = button.Button(x=WIDTH / 2 + 200, y=300, width=150, height=50, text="Enter", font_color=BLACK)


    # Player selection sprites
    num_player_select = number_slider.NumberSlider(surface=screen, x=WIDTH / 2 - 200, y=150, width=400, height=50, start=1, end=4)
    num_bot_select = number_slider.NumberSlider(surface=screen, x=WIDTH / 2 - 200, y=350, width=400, height=50, start=1, end=4)
    comfirm_player_button = button.Button(x=WIDTH / 2 - 75, y=500, width=150, height=50, text="Enter", font_color=BLACK)

    # Add sprites to the sprite groups

    # Add the start screen sprites
    start_sprites.add(create_server_button)
    start_sprites.add(create_client_button)

    # Add the request ip sprites
    request_ip_sprites.add(text_area_ip)
    request_ip_sprites.add(comfirm_ip_button)

    # Add the player selection sprites
    player_selection_sprites.add(num_player_select)
    player_selection_sprites.add(num_bot_select)
    player_selection_sprites.add(comfirm_player_button)


    # Create variables used in the loop
    running = True
    action = None

    # Start screen game loop
    while running:     # For the start screen
        #Keep loop running at the right speed
        clock.tick(FPS)
        # Process input(events)
        for event in pygame.event.get():
            #Check for closing window
            if event.type == pygame.QUIT:
                running = False

        #Draw/Render
        screen.fill(GREEN)

        # Draw the title
        functions.draw_image(screen, images["start_title"], WIDTH / 2 - 350, 0)

        #Blit the sprites
        start_sprites.draw(screen)

        # Check for button press
        if create_server_button.is_clicked():
            action = "Server"
            running = False
        elif create_client_button.is_clicked():
            action = "Client"
            running = False

        pygame.display.flip()

    # Kill the start sprites
    for sprite in start_sprites:
        sprite.kill()

    # The next window
    if action == "Client":
        # The ip address window
        running = True
        while running:
            #Keep loop running at the right speed
            clock.tick(FPS)

            # Process input(events)
            for event in pygame.event.get():
                #Check for closing window
                if event.type == pygame.QUIT:
                    running = False
                # Check for key presses
                if event.type == pygame.KEYDOWN:
                    text_area_ip.typed_key(event.key)

            #Draw/Render
            screen.fill(GREEN)

            # Draw some of the background
            functions.draw_image(screen, images["card_background_1"], 0, 0)

            #Blit the sprites
            request_ip_sprites.draw(screen)

            # Update the sprites
            text_area_ip.update()

            # Make the ip Text
            functions.draw_text(screen, WIDTH / 2, 150, "Enter the Code", size=50, color=BLACK)

            # Check for button press
            if comfirm_ip_button.is_clicked():
                ip = text_area_ip.get_value()
                if "." not in ip:
                    print("Invalid IP")
                running = False

            pygame.display.flip()
        server_ip = ip
    elif action == "Server":
        # The server design window
        running = True
        while running:
            #Keep loop running at the right speed
            clock.tick(FPS)

            # Process input(events)
            for event in pygame.event.get():
                #Check for closing window
                if event.type == pygame.QUIT:
                    running = False

            #Draw/Render
            screen.fill(GREEN)

            # Draw some of the background
            functions.draw_image(screen, images["card_background_2"], 0, 200)

            # Update the sprites
            player_selection_sprites.update()

            #Blit the sprites
            player_selection_sprites.draw(screen)

            # Make the players Text
            functions.draw_text(screen, WIDTH / 2, 100, "Select the number of players", size=50, color=BLACK)

            # Make the bots text
            functions.draw_text(screen, WIDTH / 2, 300, "Select the number of bots", size=50, color=BLACK)

            pygame.display.flip()
    

    #Close the game
    pygame.quit()


if __name__=="__main__":
    main()
