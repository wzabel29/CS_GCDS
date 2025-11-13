import pygame
import random

# Initialize Pygame
pygame.init()

# --- Configuration ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BG_COLOR = (255, 255, 255) # White
TEXT_COLOR = (0, 0, 0)     # Black
FPS = 30

# Choices
CHOICES = ["Rock", "Paper", "Scissors"]

# --- Set up the display ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# --- Fonts ---
font_large = pygame.font.Font(None, 50)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# --- Game Variables ---
player_choice = ""
computer_choice = ""
game_result = "Choose your move!"
game_active = True

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Scissors" and computer == "Paper") or \
         (player == "Paper" and computer == "Rock"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function to handle player choice
def handle_choice(choice):
    global player_choice, computer_choice, game_result, game_active
    if game_active:
        player_choice = choice
        computer_choice = random.choice(CHOICES)
        game_result = determine_winner(player_choice, computer_choice)
        game_active = False # End the round

# --- Main Game Loop ---
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check for button clicks
            if rock_button_rect.collidepoint(event.pos): handle_choice("Rock")
            elif paper_button_rect.collidepoint(event.pos):
                handle_choice("Paper")
            elif scissors_button_rect.collidepoint(event.pos):
                handle_choice("Scissors")
            elif restart_button_rect.collidepoint(event.pos) and not game_active:
                # Restart the game state
                player_choice = ""
                computer_choice = ""
                game_result = "Choose your move!"
                game_active = True


    # --- Drawing ---
    screen.fill(BG_COLOR)

    # Render Text
    title_text = font_large.render("Rock Paper Scissors", True, TEXT_COLOR)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))

    result_text = font_medium.render(game_result, True, TEXT_COLOR)
    screen.blit(result_text, (SCREEN_WIDTH // 2 - result_text.get_width() // 2, 100))

    # Display choices after a game
    if not game_active:
        choices_text = font_small.render(f"You chose: {player_choice} | Computer chose: {computer_choice}", True, TEXT_COLOR)
        screen.blit(choices_text, (SCREEN_WIDTH // 2 - choices_text.get_width() // 2, 150))


    # --- Buttons (Simple Text Buttons) ---

    # Rock Buttonrock_button_surf = font_medium.render("Rock", True, (0, 0, 0), (100, 255, 100))
    rock_button_rect = rock_button_surf.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    screen.blit(rock_button_surf, rock_button_rect)

    # Paper Button
    paper_button_surf = font_medium.render("Paper", True, (0, 0, 0), (100, 100, 255))
    paper_button_rect = paper_button_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(paper_button_surf, paper_button_rect)

    # Scissors Button
    scissors_button_surf = font_medium.render("Scissors", True, (0, 0, 0), (255, 100, 100))
    scissors_button_rect = scissors_button_surf.get_rect(center=(SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT // 2))
    screen.blit(scissors_button_surf, scissors_button_rect)
    
    # Restart Button (only visible after a game)
    if not game_active:
        restart_button_surf = font_medium.render("Play Again?", True, (0, 0, 0), (200, 200, 200))
        restart_button_rect = restart_button_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4))
        screen.blit(restart_button_surf, restart_button_rect)


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()