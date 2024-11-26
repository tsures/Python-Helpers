import pyaudio
import numpy as np
import pygame
import math

# הגדרות לדגימת הסאונד
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# הגדרות לתצוגה
WIDTH = 400
HEIGHT = 300
NEEDLE_LENGTH = 100
CENTER = (WIDTH // 2, HEIGHT - 50)

# אתחול pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sound Meter")
clock = pygame.time.Clock()

# אתחול PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def get_sound_level():
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    return np.abs(data).mean()

def draw_needle(angle):
    end_pos = (
        CENTER[0] + NEEDLE_LENGTH * math.cos(angle),
        CENTER[1] - NEEDLE_LENGTH * math.sin(angle)
    )
    pygame.draw.line(screen, (255, 0, 0), CENTER, end_pos, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # קבלת רמת הסאונד
    level = get_sound_level()
    
    # המרת רמת הסאונד לזווית (0 עד pi)
    angle = np.interp(level, [0, 5000], [0, math.pi])

    # ציור המסך
    screen.fill((255, 255, 255))
    pygame.draw.arc(screen, (0, 0, 0), [50, HEIGHT-200, WIDTH-100, 200], 0, math.pi, 2)
    draw_needle(angle)

    pygame.display.flip()
    clock.tick(30)

# ניקוי וסגירה
stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()