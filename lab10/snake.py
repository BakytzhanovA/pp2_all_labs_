import sqlite3
import json
import pygame
import random
import sys

# Инициализация базы данных
class SnakeGameDB:
    def __init__(self, db_name='snake_game.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_score (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                level INTEGER NOT NULL DEFAULT 1,
                score INTEGER NOT NULL DEFAULT 0,
                saved_state TEXT,
                last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id)
            )
        ''')
        self.conn.commit()
    
    def get_or_create_user(self, username):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id FROM user WHERE username = ?', (username,))
        user = cursor.fetchone()
        
        if user:
            user_id = user[0]
            cursor.execute('''
                SELECT level, score, saved_state 
                FROM user_score 
                WHERE user_id = ? 
                ORDER BY last_played DESC 
                LIMIT 1
            ''', (user_id,))
            score_data = cursor.fetchone()
            
            if score_data:
                level, score, saved_state = score_data
                print(f"Добро пожаловать назад, {username}! Ваш уровень: {level}, последний счет: {score}")
                return user_id, level, score, saved_state
            else:
                print(f"Добро пожаловать назад, {username}! Начинаем с уровня 1")
                return user_id, 1, 0, None
        else:
            cursor.execute('INSERT INTO user (username) VALUES (?)', (username,))
            user_id = cursor.lastrowid
            self.conn.commit()
            print(f"Новый пользователь {username} создан. Начинаем с уровня 1")
            return user_id, 1, 0, None
    
    def save_game_state(self, user_id, level, score, game_state):
        game_state_json = json.dumps(game_state)
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO user_score (user_id, level, score, saved_state)
            VALUES (?, ?, ?, ?)
        ''', (user_id, level, score, game_state_json))
        self.conn.commit()
    
    def close(self):
        self.conn.close()

# Игра "Змейка"
class SnakeGame:
    def __init__(self, username, level=1, saved_state=None):
        self.username = username
        self.level = level
        self.saved_state = saved_state
        
        # Настройки уровня
        self.speeds = {1: 10, 2: 15, 3: 20}
        self.colors = {1: (0, 255, 0), 2: (0, 200, 0), 3: (0, 150, 0)}
        
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(f'Змейка | Пользователь: {username} | Уровень: {level}')
        
        self.clock = pygame.time.Clock()
        self.FPS = self.speeds.get(level, 10)
        self.snake_color = self.colors.get(level, (0, 255, 0))
        
        # Инициализация змейки из сохранения или новая
        if saved_state:
            try:
                state = json.loads(saved_state)
                self.snake = state.get("snake_position", [[100, 100], [90, 100], [80, 100]])
                self.direction = state.get("direction", "RIGHT")
                self.score = state.get("score", 0)
                self.food_pos = state.get("food_position", self.generate_food())
                self.size = len(self.snake)
            except json.JSONDecodeError:
                self.reset_game()
        else:
            self.reset_game()
    
    def reset_game(self):
        self.snake = [[100, 100], [90, 100], [80, 100]]
        self.direction = "RIGHT"
        self.score = 0
        self.size = 3
        self.food_pos = self.generate_food()
    
    def generate_food(self):
        return [random.randrange(1, self.WIDTH//10) * 10, 
                random.randrange(1, self.HEIGHT//10) * 10]
    
    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.screen, self.snake_color, [segment[0], segment[1], 10, 10])
    
    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), [self.food_pos[0], self.food_pos[1], 10, 10])
    
    def move_snake(self):
        head = self.snake[0].copy()
        
        if self.direction == "RIGHT":
            head[0] += 10
        elif self.direction == "LEFT":
            head[0] -= 10
        elif self.direction == "UP":
            head[1] -= 10
        elif self.direction == "DOWN":
            head[1] += 10
        
        # Проверка на выход за границы
        if head[0] >= self.WIDTH or head[0] < 0 or head[1] >= self.HEIGHT or head[1] < 0:
            self.game_over()
            return False
        
        # Проверка на самопоедание
        if head in self.snake[1:]:
            self.game_over()
            return False
        
        self.snake.insert(0, head)
        if len(self.snake) > self.size:
            self.snake.pop()
        
        # Проверка на еду
        if head == self.food_pos:
            self.size += 1
            self.score += 10
            self.food_pos = self.generate_food()
        
        return True
    
    def game_over(self):
        font = pygame.font.SysFont(None, 72)
        text = font.render('Игра окончена!', True, (255, 0, 0))
        self.screen.blit(text, (self.WIDTH//2 - 150, self.HEIGHT//2 - 36))
        pygame.display.update()
        pygame.time.wait(2000)
    
    def run(self, db):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                    elif event.key == pygame.K_p:  # Сохранение игры
                        game_state = {
                            "snake_position": self.snake,
                            "direction": self.direction,
                            "score": self.score,
                            "food_position": self.food_pos
                        }
                        db.save_game_state(db_user_id, self.level, self.score, game_state)
                        print("Игра сохранена! Нажмите любую клавишу для продолжения...")
            
            if not self.move_snake():
                running = False
            
            self.screen.fill((0, 0, 0))
            self.draw_snake()
            self.draw_food()
            
            # Отображение счета
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f'Счет: {self.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
            
            pygame.display.update()
            self.clock.tick(self.FPS)
        
        pygame.quit()

# Основная программа
if __name__ == "__main__":
    # Запрос имени пользователя
    username = input("Введите ваше имя: ")
    
    # Работа с базой данных
    db = SnakeGameDB()
    db_user_id, level, score, saved_state = db.get_or_create_user(username)
    
    # Запуск игры
    game = SnakeGame(username, level, saved_state)
    game.run(db)
    
    # Закрытие базы данных
    db.close()