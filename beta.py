import pygame

# Inicializáljuk a Pygame-et
pygame.init()

# Ablak mérete
width, height = 800, 600

# Ablak létrehozása
screen = pygame.display.set_mode((width, height))

# Ablak címe
pygame.display.set_caption("Zöldes-Kékes Háttér")

# Háttérszín beállítása
background_color = (0, 128, 128)  # Zöldes-kékes szín RGB kóddal

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ablak háttérszínének beállítása
    screen.fill(background_color)

    # Itt hozzáadhatsz további rajzolási és logikai műveleteket

    # Frissítjük az ablakot
    pygame.display.flip()

# Pygame leállítása
pygame.quit()
