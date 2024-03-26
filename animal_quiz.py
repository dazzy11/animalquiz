import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animal Sound Quiz")

dog_sound = pygame.mixer.Sound("dog.wav")
cat_sound = pygame.mixer.Sound("cat.wav")
cow_sound = pygame.mixer.Sound("cow.wav")
duck_sound = pygame.mixer.Sound("duck.wav")

animal_sounds = {
    "dog": dog_sound,
    "cat": cat_sound,
    "cow": cow_sound,
    "duck": duck_sound,
}

animals = list(animal_sounds.keys())

score = 0

font = pygame.font.Font(None, 36)

def display_text(text, color, pos):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect)

def display_options(options):
    option_x = 100
    option_y = screen_height // 2
    for option in options:
        option_text = font.render(option.capitalize(), True, BLACK)
        option_rect = option_text.get_rect(center=(option_x, option_y))
        pygame.draw.rect(screen, GRAY, option_rect.inflate(20, 10))
        screen.blit(option_text, option_rect)
        option_x += 200

def generate_options(correct_answer):
    options = [correct_answer]
    while len(options) < 4:
        random_option = random.choice(animals)
        if random_option not in options:
            options.append(random_option)
    random.shuffle(options)
    return options

running = True
while running:
    screen.fill(WHITE)

    current_animal = random.choice(animals)
    current_sound = animal_sounds[current_animal]
    current_sound.play()

    display_text("Guess the Animal!", BLACK, (screen_width // 2, 100))

    options = generate_options(current_animal)
    display_options(options)

    pygame.display.flip()

    pygame.time.wait(int(current_sound.get_length() * 1000))
    current_sound.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            option_index = (mouse_pos[0] - 100) // 200
            if 0 <= option_index < len(options):
                selected_option = options[option_index]
                if selected_option == current_animal:
                    score += 1
                running = False

screen.fill(WHITE)
display_text(f"Final Score: {score}", BLACK, (screen_width // 2, screen_height // 2))
pygame.display.flip()

pygame.time.wait(9000)
pygame.quit()
