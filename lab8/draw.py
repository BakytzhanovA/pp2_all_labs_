import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Графический редактор с удалением")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (200, 200, 200)

# Текущий цвет
current_color = BLACK

# Режимы рисования
DRAW_RECT = 0
DRAW_CIRCLE = 1
ERASER = 2
DELETE = 3
current_mode = DRAW_RECT

# Радиус кисти/ластика
brush_size = 5

# Панель инструментов
toolbar_rect = pygame.Rect(0, 0, WIDTH, 80)
button_size = 50
button_margin = 10

# Кнопки инструментов
buttons = [
    {"rect": pygame.Rect(10, 10, button_size, button_size), "color": GRAY, "mode": DRAW_RECT, "text": "□"},
    {"rect": pygame.Rect(70, 10, button_size, button_size), "color": GRAY, "mode": DRAW_CIRCLE, "text": "○"},
    {"rect": pygame.Rect(130, 10, button_size, button_size), "color": GRAY, "mode": ERASER, "text": "E"},
    {"rect": pygame.Rect(190, 10, button_size, button_size), "color": GRAY, "mode": DELETE, "text": "DEL"},
]

# Кнопки цветов
color_buttons = [
    {"rect": pygame.Rect(260, 10, button_size, button_size), "color": BLACK},
    {"rect": pygame.Rect(320, 10, button_size, button_size), "color": RED},
    {"rect": pygame.Rect(380, 10, button_size, button_size), "color": GREEN},
    {"rect": pygame.Rect(440, 10, button_size, button_size), "color": BLUE},
    {"rect": pygame.Rect(500, 10, button_size, button_size), "color": YELLOW},
    {"rect": pygame.Rect(560, 10, button_size, button_size), "color": CYAN},
    {"rect": pygame.Rect(620, 10, button_size, button_size), "color": MAGENTA},
]

# Основной цикл
clock = pygame.time.Clock()
drawing = False
start_pos = (0, 0)
objects = []
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    
    # Рисуем панель инструментов
    pygame.draw.rect(screen, GRAY, toolbar_rect)
    
    # Рисуем кнопки инструментов
    for button in buttons:
        color = button["color"]
        if button["mode"] == current_mode:
            color = (min(color[0] + 50, 255), min(color[1] + 50, 255), min(color[2] + 50, 255))
        
        pygame.draw.rect(screen, color, button["rect"])
        pygame.draw.rect(screen, BLACK, button["rect"], 2)
        
        font = pygame.font.SysFont(None, 36)
        text = font.render(button["text"], True, BLACK)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)
    
    # Рисуем кнопки цветов
    for c_button in color_buttons:
        pygame.draw.rect(screen, c_button["color"], c_button["rect"])
        pygame.draw.rect(screen, BLACK, c_button["rect"], 2)
        
        if c_button["color"] == current_color:
            pygame.draw.rect(screen, WHITE, c_button["rect"], 4)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Обработка кликов мышкой
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                pos = event.pos
                
                # Проверяем клик по кнопкам инструментов
                for button in buttons:
                    if button["rect"].collidepoint(pos):
                        current_mode = button["mode"]
                
                # Проверяем клик по кнопкам цветов
                for c_button in color_buttons:
                    if c_button["rect"].collidepoint(pos):
                        current_color = c_button["color"]
                
                # Если клик не на панели инструментов, начинаем рисование
                if pos[1] > toolbar_rect.height:
                    if current_mode == DELETE:
                        # Удаляем фигуры, начиная с последней
                        for i in range(len(objects)-1, -1, -1):
                            obj = objects[i]
                            if obj[0] == 'rect' and obj[1].collidepoint(pos):
                                del objects[i]
                                break
                            elif obj[0] == 'circle':
                                distance = ((pos[0] - obj[1][0])**2 + (pos[1] - obj[1][1])**2)**0.5
                                if distance <= obj[2]:
                                    del objects[i]
                                    break
                        # Перерисовываем canvas
                        canvas.fill(WHITE)
                        for obj in objects:
                            if obj[0] == 'rect':
                                pygame.draw.rect(canvas, obj[2], obj[1], 2)
                            elif obj[0] == 'circle':
                                pygame.draw.circle(canvas, obj[3], obj[1], obj[2], 2)
                    else:
                        drawing = True
                        start_pos = pos
                        
                        if current_mode == ERASER:
                            pygame.draw.circle(canvas, WHITE, pos, brush_size)
                            pygame.display.update()
        
        # Рисование
        elif event.type == pygame.MOUSEMOTION:
            if drawing and event.pos[1] > toolbar_rect.height:
                if current_mode == ERASER:
                    pygame.draw.circle(canvas, WHITE, event.pos, brush_size)
                    pygame.display.update()
        
        # Завершение рисования
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing and event.pos[1] > toolbar_rect.height:
                drawing = False
                end_pos = event.pos
                
                # Добавляем объект в список
                if current_mode == DRAW_RECT:
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), 
                                     min(start_pos[1], end_pos[1]), 
                                     abs(end_pos[0] - start_pos[0]), 
                                     abs(end_pos[1] - start_pos[1]))
                    objects.append(('rect', rect, current_color))
                    pygame.draw.rect(canvas, current_color, rect, 2)
                
                elif current_mode == DRAW_CIRCLE:
                    radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                    objects.append(('circle', start_pos, radius, current_color))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
        
        # Изменение размера кисти колесиком мыши
        elif event.type == pygame.MOUSEWHEEL:
            brush_size = max(1, brush_size + event.y)
    
    # Отображение информации о текущем режиме и размере кисти
    font = pygame.font.SysFont(None, 24)
    mode_text = f"Режим: {'Прямоугольник' if current_mode == DRAW_RECT else 'Круг' if current_mode == DRAW_CIRCLE else 'Ластик' if current_mode == ERASER else 'Удаление'}"
    size_text = f"Размер: {brush_size} (колесико мыши)"
    
    text_surface = font.render(mode_text, True, BLACK)
    screen.blit(text_surface, (10, HEIGHT - 30))
    
    text_surface = font.render(size_text, True, BLACK)
    screen.blit(text_surface, (200, HEIGHT - 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()