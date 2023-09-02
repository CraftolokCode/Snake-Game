import pygame
import sys
import random

# Inicializáljuk a Pygame-et
pygame.init()

# Ablak mérete
width, height = 800, 600

# Ablak létrehozása
screen = pygame.display.set_mode((width, height))

# Ablak címe
pygame.display.set_caption("Snake Játék")

# Színek
background_color = (0, 0, 0)  # Fekete háttérszín
snake_color = (0, 255, 0)  # Zöld szín a kígyónak
food_color = (255, 0, 0)  # Piros szín az ételnek
text_color = (255, 255, 255)  # Fehér szín a szövegnek

# Snake kezdeti pozíció
snake_x, snake_y = width // 2, height // 2

# Snake mozgás irányai
snake_dx, snake_dy = 0, 0

# Snake hossza és teste
snake_length = 1
snake_body = [(snake_x, snake_y)]

# Étel pozíciója
food_x, food_y = random.randint(0, (width - 20) // 20) * 20, random.randint(0, (height - 20) // 20) * 20

# Játéksebesség
game_speed = 75  # A játék most 75 milliszekundumonként frissül

# Pontszám számláló
score = 0

font = pygame.font.Font(None, 36)

# Játék állapotok
IDLE = 0
PLAYING = 1
PAUSED = 2
GAME_OVER = 3

# Kezdeti állapot
game_state = IDLE

# Főciklus és játék indítása
def main():
    global snake_x, snake_y, snake_dx, snake_dy, snake_length, snake_body, food_x, food_y, game_speed, score, game_state

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == IDLE:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = PLAYING
                        initialize_game()
            elif game_state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_state = PAUSED
                    elif event.key == pygame.K_UP and snake_dy == 0:
                        snake_dx, snake_dy = 0, -20
                    elif event.key == pygame.K_DOWN and snake_dy == 0:
                        snake_dx, snake_dy = 0, 20
                    elif event.key == pygame.K_LEFT and snake_dx == 0:
                        snake_dx, snake_dy = -20, 0
                    elif event.key == pygame.K_RIGHT and snake_dx == 0:
                        snake_dx, snake_dy = 20, 0
                # További játéklogika
            elif game_state == PAUSED:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_state = PLAYING
                # További játéklogika
            elif game_state == GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_state = IDLE

        screen.fill(background_color)

        if game_state == IDLE:
            # Kiírjuk a kezdeti üzenetet
            draw_text("Snake Játék", font, text_color, width // 2, height // 4)
            draw_text("Nyomd meg a SPACE-t a játék indításához", font, text_color, width // 2, height // 2)
        elif game_state == PLAYING:
            # Játék folyik
            move_snake()
            check_collision()
            draw_snake()
            draw_food()
            draw_score()
        elif game_state == PAUSED:
            # Játék szüneteltetve
            draw_text("Szünet (Nyomd meg a P-t a folytatáshoz)", font, text_color, width // 2, height // 2)
        elif game_state == GAME_OVER:
            # Játék vége
            draw_text("Játék vége (Nyomd meg az R-t az újraindításhoz)", font, text_color, width // 2, height // 2)

        pygame.display.flip()
        pygame.time.delay(game_speed)

    pygame.quit()
    sys.exit()

def initialize_game():
    global snake_x, snake_y, snake_dx, snake_dy, snake_length, snake_body, food_x, food_y, score
    snake_x, snake_y = width // 2, height // 2
    snake_dx, snake_dy = 0, 0
    snake_length = 1
    snake_body = [(snake_x, snake_y)]
    food_x, food_y = random.randint(0, (width - 20) // 20) * 20, random.randint(0, (height - 20) // 20) * 20
    score = 0

def move_snake():
    global snake_x, snake_y, snake_body
    snake_x += snake_dx
    snake_y += snake_dy
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

def check_collision():
    global snake_x, snake_y, snake_length, food_x, food_y, score, game_state
    if (snake_x, snake_y) in snake_body[:-1] or snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        game_state = GAME_OVER
    if snake_x == food_x and snake_y == food_y:
        snake_length += 1
        food_x, food_y = random.randint(0, (width - 20) // 20) * 20, random.randint(0, (height - 20) // 20) * 20
        score += 1

def draw_snake():
    for segment in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0], segment[1], 20, 20))

def draw_food():
    pygame.draw.rect(screen, food_color, pygame.Rect(food_x, food_y, 20, 20))

def draw_score():
    draw_text(f"Pontszám: {score}", font, text_color, width // 2, 10)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

if __name__ == "__main__":
    main()
