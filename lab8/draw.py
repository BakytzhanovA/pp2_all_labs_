import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App with Shapes and Eraser")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [BLACK, RED, GREEN, BLUE]

# переменные для рисования
current_color = BLACK
drawing = False
tool = "pen"  # Текущий инструмент (pen, rect, circle, eraser)
start_pos = None

# список объектов, которые мы рисуем
shapes = []

# Шрифт для текста
font = pygame.font.Font(None, 36)

# Классы для кнопок
class Button:
    def __init__(self, x, y, width, height, color, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Класс для фигур (Прямоугольник и круг)
class Shape:
    def __init__(self, shape_type, color, position):
        self.shape_type = shape_type  # 'rect' или 'circle'
        self.color = color
        self.position = position
        if self.shape_type == "rect":
            self.width = 100
            self.height = 50
        elif self.shape_type == "circle":
            self.radius = 50

    def draw(self, screen):
        if self.shape_type == "rect":
            pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.width, self.height))
        elif self.shape_type == "circle":
            pygame.draw.circle(screen, self.color, self.position, self.radius)
    
    def collidepoint(self, pos):
        """Проверка, попадает ли точка в фигуру."""
        if self.shape_type == "rect":
            rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
            return rect.collidepoint(pos)
        elif self.shape_type == "circle":
            distance = ((pos[0] - self.position[0]) ** 2 + (pos[1] - self.position[1]) ** 2) ** 0.5
            return distance <= self.radius
        return False

# для рисования на экране
def draw_shape(start_pos, end_pos):
    if tool == "pen":
        pygame.draw.line(screen, current_color, start_pos, end_pos, 3)

# цикл игры
screen.fill(WHITE)

# кнопки для выбора цвета
color_buttons = [
    Button(20, HEIGHT - 60, 50, 50, BLACK, "Black", lambda: set_color(BLACK)),
    Button(80, HEIGHT - 60, 50, 50, RED, "Red", lambda: set_color(RED)),
    Button(140, HEIGHT - 60, 50, 50, GREEN, "Green", lambda: set_color(GREEN)),
    Button(200, HEIGHT - 60, 50, 50, BLUE, "Blue", lambda: set_color(BLUE)),
]

shape_buttons = [
    Button(300, HEIGHT - 60, 50, 50, BLACK, "Rect", lambda: set_tool("rect")),
    Button(360, HEIGHT - 60, 50, 50, BLACK, "Circle", lambda: set_tool("circle")),
]

eraser_button = Button(420, HEIGHT - 60, 50, 50, BLACK, "Erase", lambda: set_tool("eraser"))

def set_color(color):
    global current_color
    current_color = color

def set_tool(selected_tool):
    global tool
    tool = selected_tool

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            
            if any(button.is_clicked(event.pos) for button in color_buttons):
                for button in color_buttons:
                    if button.is_clicked(event.pos):
                        button.action()  
            elif any(button.is_clicked(event.pos) for button in shape_buttons):
                for button in shape_buttons:
                    if button.is_clicked(event.pos):
                        button.action()  # (изменение инструмента)
            elif eraser_button.is_clicked(event.pos):
                eraser_button.action()  # Включаем ластик
            elif tool in ["rect", "circle"]:
                new_shape = Shape(tool, current_color, event.pos)
                shapes.append(new_shape)

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pen":
                draw_shape(start_pos, event.pos)
                start_pos = event.pos

        if tool == "eraser" and event.type == pygame.MOUSEBUTTONDOWN:
            for shape in shapes[:]:
                if shape.collidepoint(event.pos):
                    shapes.remove(shape)  

    for button in color_buttons:
        button.draw(screen)
    
    for button in shape_buttons:
        button.draw(screen)
    
    eraser_button.draw(screen)

    for shape in shapes:
        shape.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

