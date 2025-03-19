import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

playlist = [
    "Lucaveros - Накроет Волной.mp3",  
    "Ulukmanapo - Летали.mp3"  
]

pygame.mixer.init()

current_song_index = 0

pygame.mixer.music.load(playlist[current_song_index])

is_playing = False

def play_music():
    pygame.mixer.music.play()
    global is_playing
    is_playing = True

def stop_music():
    pygame.mixer.music.stop()
    global is_playing
    is_playing = False

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song_index])
    play_music()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song_index])
    play_music()

def draw_buttons():
    pygame.draw.rect(screen, (0, 255, 0), (50, 150, 60, 30))  
    font = pygame.font.SysFont(None, 24)
    play_text = font.render("Play", True, (0, 0, 0))
    screen.blit(play_text, (60, 155))

    pygame.draw.rect(screen, (255, 0, 0), (130, 150, 60, 30))  
    stop_text = font.render("Stop", True, (0, 0, 0))
    screen.blit(stop_text, (140, 155))

    pygame.draw.rect(screen, (0, 0, 255), (210, 150, 60, 30))  
    next_text = font.render("Next", True, (0, 0, 0))
    screen.blit(next_text, (220, 155))

    pygame.draw.rect(screen, (255, 255, 0), (290, 150, 60, 30))  
    prev_text = font.render("Prev", True, (0, 0, 0))
    screen.blit(prev_text, (300, 155))

def check_button_click(pos):
    global is_playing
    if 50 <= pos[0] <= 110 and 150 <= pos[1] <= 180:  
        if not is_playing:
            play_music()
    elif 130 <= pos[0] <= 190 and 150 <= pos[1] <= 180: 
        if is_playing:
            stop_music()
    elif 210 <= pos[0] <= 270 and 150 <= pos[1] <= 180:  
        if is_playing:
            next_song()
    elif 290 <= pos[0] <= 350 and 150 <= pos[1] <= 180:  
        if is_playing:
            prev_song()

while True:
    screen.fill((255, 255, 255)) 
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            check_button_click(pos)

    pygame.display.update()
