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

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0], segment[1], 20, 20))

def draw_score():
    score_text = font.render(f"Pontszám: {score}", True, text_color)
    text_rect = score_text.get_rect()
    text_rect.topleft = (width // 2 - text_rect.width // 2, 10)
    screen.blit(score_text, text_rect)

# Indítógomb színe és pozíciója
button_color = (0, 128, 255)  # Kék gomb színe
button_width, button_height = 200, 50
button_x = width // 2 - button_width // 2
button_y = height // 2 - button_height // 2
button_text = font.render("Játék indítása", True, text_color)

# Főciklus és játék indítása
def main():
    global snake_x, snake_y, snake_dx, snake_dy, snake_length, snake_body, food_x, food_y, game_speed, score

    running = True
    game_started = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_dx, snake_dy = 0, -20
                if event.key == pygame.K_DOWN:
                    snake_dx, snake_dy = 0, 20
                if event.key == pygame.K_LEFT:
                    snake_dx, snake_dy = -20, 0
                if event.key == pygame.K_RIGHT:
                    snake_dx, snake_dy = 20, 0
            if event.type == pygame.MOUSEBUTTONDOWN and not game_started:
                if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                    game_started = True

        if game_started:
            snake_x += snake_dx
            snake_y += snake_dy

            # Ha a kígyó eléri az ablak szélét, akkor a másik oldalon jelenik meg
            if snake_x < 0:
                snake_x = width - 20
            elif snake_x >= width:
                snake_x = 0
            elif snake_y < 0:
                snake_y = height - 20
            elif snake_y >= height:
                snake_y = 0

            # Ellenőrizzük, hogy a kígyó ütközik-e saját testébe
            if (snake_x, snake_y) in snake_body[:-1]:
                running = False

            snake_body.append((snake_x, snake_y))

            # Ellenőrizzük, hogy a kígyó megeszi-e az ételt
            if pygame.Rect(snake_x, snake_y, 20, 20).colliderect(pygame.Rect(food_x, food_y, 20, 20)):
                snake_length += 1
                food_x, food_y = random.randint(0, (width - 20) // 20) * 20, random.randint(0, (height - 20) // 20) * 20
                score += 1

            # A kígyó hosszát beállítjuk
            if len(snake_body) > snake_length:
                del snake_body[0]

        screen.fill(background_color)

        if not game_started:
            pygame.draw.rect(screen, button_color, pygame.Rect(button_x, button_y, button_width, button_height))
            screen.blit(button_text, (button_x + 20, button_y + 10))
        else:
            # Kígyó rajzolása
            draw_snake(snake_body)

            # Étel rajzolása
            pygame.draw.rect(screen, food_color, pygame.Rect(food_x, food_y, 20, 20))

            # Pontszám számláló rajzolása
            draw_score()

        # Frissítjük az ablakot
        pygame.display.flip()

        # Várunk egy rövid ideig, hogy a játék sebessége ne legyen túl gyors
        pygame.time.delay(game_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
