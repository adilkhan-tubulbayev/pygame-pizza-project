import pygame
import sys
import random
import time

# Инициализация pygame
pygame.init()

# Настройка окна игры
pygame.display.set_caption("Sabi's Pizza game")
window = pygame.display.set_mode((1920, 1080))

# Загрузка фоновых изображений
menu_scene_background_image = pygame.image.load('assets/pizzeria_theme.png')
menu_scene_background_image_scaled = pygame.transform.scale(menu_scene_background_image, (1920, 1080))
game_scene_background_color = pygame.Color('#FAE6D9')

# Загрузка и масштабирование ингредиентов с прямоугольниками
basil_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/basil.png'), (200, 100))
basil_rect = basil_scaled.get_rect()

cheddar_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/cheddar.png'), (200, 100))
cheddar_rect = cheddar_scaled.get_rect()

egg_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/egg.png'), (200, 100))
egg_rect = egg_scaled.get_rect()

gorgonzola_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/gorgonzola.png'), (200, 100))
gorgonzola_rect = gorgonzola_scaled.get_rect()

mushroom_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/mushroom.png'), (200, 100))
mushroom_rect = mushroom_scaled.get_rect()

pepperoni_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/pepperoni.png'), (200, 100))
pepperoni_rect = pepperoni_scaled.get_rect()

tomato_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/tomato.png'), (200, 100))
tomato_rect = tomato_scaled.get_rect()

cheese_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/cheese.png'), (200, 100))
cheese_rect = cheese_scaled.get_rect()

bacon_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/bacon.png'), (200, 100))
bacon_rect = bacon_scaled.get_rect()

onion_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/onion.png'), (200, 100))
onion_rect = onion_scaled.get_rect()

ham_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/ham.png'), (200, 100))
ham_rect = ham_scaled.get_rect()

sausage_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/sausage.png'), (200, 100))
sausage_rect = sausage_scaled.get_rect()

olives_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/olives.png'), (200, 100))
olives_rect = olives_scaled.get_rect()

chicken_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/chicken.png'), (200, 100))
chicken_rect = chicken_scaled.get_rect()

lettuce_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/lettuce.png'), (200, 100))
lettuce_rect = lettuce_scaled.get_rect()

shrimp_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/shrimp.png'), (200, 100))
shrimp_rect = shrimp_scaled.get_rect()

mussels_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/mussels.png'), (200, 100))
mussels_rect = mussels_scaled.get_rect()

squid_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/squid.png'), (200, 100))
squid_rect = squid_scaled.get_rect()

jalapeno_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/jalapeno.png'), (200, 100))
jalapeno_rect = jalapeno_scaled.get_rect()

testo_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/testo.png'), (900, 400))
testo_rect = testo_scaled.get_rect(topleft=(500, 500))

oven_scaled = pygame.transform.scale(pygame.image.load('assets/easy_pizza_ingredients/oven.png'), (500, 400))
oven_rect = oven_scaled.get_rect(topleft=(1350, 500))

# Список всех ингредиентов
ingredient_list = [
    'basil', 'cheddar', 'egg', 'gorgonzola', 'mushroom', 'pepperoni', 'tomato',
    'cheese', 'bacon', 'onion', 'ham', 'sausage', 'olives', 'chicken', 'lettuce',
    'shrimp', 'mussels', 'squid', 'jalapeno'
]

# Списки изображений и прямоугольников для всех ингредиентов
all_ingredients_image_list = [
    basil_scaled, cheddar_scaled, egg_scaled, gorgonzola_scaled, mushroom_scaled,
    pepperoni_scaled, tomato_scaled, cheese_scaled, bacon_scaled, onion_scaled,
    ham_scaled, sausage_scaled, olives_scaled, chicken_scaled, lettuce_scaled,
    shrimp_scaled, mussels_scaled, squid_scaled, jalapeno_scaled
]

all_ingredients_rect_list = [
    basil_rect, cheddar_rect, egg_rect, gorgonzola_rect, mushroom_rect,
    pepperoni_rect, tomato_rect, cheese_rect, bacon_rect, onion_rect,
    ham_rect, sausage_rect, olives_rect, chicken_rect, lettuce_rect,
    shrimp_rect, mussels_rect, squid_rect, jalapeno_rect
]

# Обновление списка имен ингредиентов
ingredient_names = ingredient_list

# **Настраиваемые параметры позиционирования ингредиентов**
# ------------------------------------------------------------------------------
# Изменяйте эти значения, чтобы настроить расположение ингредиентов на экране
column1_x = 100  # X-координата для левой колонки
column2_x = 300  # X-координата для средней колонки
column3_x = 500  # X-координата для правой колонки
start_y = 200    # Начальная Y-координата для верхнего ингредиента
y_step = 120     # Расстояние между ингредиентами по Y в колонках

# Генерация начальных позиций для 19 ингредиентов: 7 в первой, 6 во второй, 6 в третьей колонке
initial_positions = (
    [(column1_x, start_y + i * y_step) for i in range(7)] +  # Первая колонка
    [(column2_x, start_y + i * y_step) for i in range(6)] +  # Вторая колонка
    [(column3_x, start_y + i * y_step) for i in range(6)]    # Третья колонка
)

# Рецепты пицц
easy_pizzas = {
    "Маргарита": ["tomato", "cheese", "basil"],
    "4 сыра": ["cheddar", "gorgonzola", "cheese"],
    "Пепперони": ["tomato", "cheese", "pepperoni"],
    "Мимоза": ["tomato", "cheese", "egg", "mushroom"]
}

medium_pizzas = {
    "Карбонара": ["cheese", "egg", "bacon"],
    "Неаполитанская": ["tomato", "cheese", "basil"],
    "Фермерская": ["tomato", "cheese", "mushroom", "onion", "ham"],
    "Мясная": ["tomato", "cheese", "pepperoni", "bacon", "sausage"],
    "Грибы и Ветчина": ["mushroom", "cheese", "ham"]
}

hard_pizzas = {
    "4 сезона": ["tomato", "cheese", "mushroom", "ham", "olives"],
    "Цезарь": ["cheese", "chicken", "lettuce", "egg"],
    "Пицца с морепродуктами": ["tomato", "cheese", "shrimp", "mussels", "squid"],
    "Острая Барбекю": ["tomato", "cheese", "pepperoni", "jalapeno", "onion"],
    "Веган": ["tomato", "mushroom", "onion", "olives"]
}

# Игровые переменные
current_level = 1
level_times = [30000, 60000, 100000]  # Время в миллисекундах: 30с, 60с, 100с
required_coins = [1, 10, 21]  # Необходимые монеты для перехода
start_time = pygame.time.get_ticks()
coins = 0
placed_ingredients = set()
placed_rects = []
feedback_message = ""
feedback_timer = 0
MAX_FEEDBACK_TIME = 2000
pizza_ready = False
dragging = False
pizza_in_oven = False
baking_start_time = 0
active_ingredient = None
current_game_scene = 'menu'
button_values = []
offset_x, offset_y = 0, 0
pizza_correct = False

# Выбор новой пиццы в зависимости от уровня
def select_new_pizza():
    global pizza_name, pizza_ingredients, placed_ingredients, placed_rects, pizza_ready, pizza_correct
    if current_level == 1:
        pizzas = easy_pizzas
    elif current_level == 2:
        pizzas = {**easy_pizzas, **medium_pizzas}
    else:
        pizzas = {**easy_pizzas, **medium_pizzas, **hard_pizzas}
    pizza_name = random.choice(list(pizzas.keys()))
    pizza_ingredients = pizzas[pizza_name]
    placed_ingredients = set()
    placed_rects = []
    pizza_ready = False
    pizza_correct = False
    reset_ingredients()

# Сброс позиций ингредиентов
def reset_ingredients():
    testo_rect.topleft = (500, 500)
    for i, rect in enumerate(all_ingredients_rect_list):
        rect.topleft = initial_positions[i]

# Сброс игры
def reset_game():
    global current_level, coins, start_time, pizza_ready, pizza_in_oven, placed_ingredients, placed_rects, active_ingredient, pizza_correct
    current_level = 1
    coins = 0
    start_time = pygame.time.get_ticks()
    pizza_ready = False
    pizza_correct = False
    pizza_in_oven = False
    placed_ingredients = set()
    placed_rects = []
    active_ingredient = None
    select_new_pizza()

# Начало нового уровня
def start_level():
    global start_time, coins
    start_time = pygame.time.get_ticks()
    coins = 0  # Сбрасываем монеты при начале нового уровня
    select_new_pizza()

# Проверка пиццы
def check_pizza():
    global pizza_correct, feedback_message, feedback_timer, pizza_ready, placed_ingredients, placed_rects
    if set(pizza_ingredients) == placed_ingredients:
        pizza_correct = True
        pizza_ready = True
        feedback_message = "Пицца готова! Перетащите её в духовку."
    else:
        pizza_correct = False
        feedback_message = "Пицца собрана неправильно!"
        placed_ingredients = set()
        placed_rects = []
        reset_ingredients()
    feedback_timer = pygame.time.get_ticks()

# Завершение выпечки
def finish_baking():
    global coins, feedback_message, feedback_timer, pizza_in_oven, pizza_ready
    pizza_in_oven = False
    coins += current_level  # Начисляем монеты в зависимости от уровня
    feedback_message = f"Пицца {pizza_name} готова! +{current_level} монет."
    feedback_timer = pygame.time.get_ticks()
    select_new_pizza()

# Вспомогательные функции для отрисовки
def draw_text(surface, text, text_size, text_color, coordinates, antialias=True):
    color = pygame.Color(text_color)
    font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', text_size)
    text_render = font.render(str(text), antialias, color, pygame.Color('#FFCDBC'))
    surface.blit(text_render, coordinates)

def draw_button_text(surface, text, text_size, text_hex_color, btn_x, btn_y, btn_width, btn_height, antialias=True):
    color = pygame.Color(text_hex_color)
    font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', text_size)
    text_render = font.render(str(text), antialias, color)
    text_x = (btn_x + btn_width // 2) - (text_render.get_width() // 2)
    text_y = (btn_y + btn_height // 2) - (text_render.get_height() // 2)
    surface.blit(text_render, (text_x, text_y))

def draw_button(surface, text, text_size, x, y, width, height, text_color='#4D261F', btn_hex_color='#FCF0DA'):
    button_rect = pygame.Rect((x, y), (width, height))
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        btn_hex_color = '#E8DCC6'
    pygame.draw.rect(surface, pygame.Color(btn_hex_color), button_rect, 0, 20)
    draw_button_text(surface, text, text_size, text_color, x, y, width, height)
    return [button_rect, text]

# Сцены
def menu_scene():
    global button_values
    window.blit(menu_scene_background_image_scaled, (0, 0))
    draw_text(window, 'Добро пожаловать в', 50, '#000000', (150, 150))
    draw_text(window, "пиццерию Sabi's Pizza", 60, '#000000', (150, 200))
    button_values = [
        draw_button(window, 'Начать игру', 25, 150, 300, 400, 100),
        draw_button(window, 'Выйти', 25, 150, 420, 400, 100),
    ]
    return button_values

def game_scene():
    global pizza_in_oven, feedback_message, feedback_timer, button_values
    window.fill(game_scene_background_color)
    
    # Информация об игре
    draw_text(window, f'Количество монет: {coins}', 30, '#FCBA04', (20, 20))
    draw_text(window, f'Уровень: {current_level}', 30, '#000000', (20, 60))
    
    # Время
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = (level_times[current_level - 1] - elapsed_time) / 1000
    if remaining_time < 0:
        remaining_time = 0
    draw_text(window, f'Осталось времени: {remaining_time:.1f} сек', 30, '#000000', (20, 100))
    
    # Информация о пицце
    draw_text(window, f'Пицца: {pizza_name}', 50, '#000000', (700, 150))
    draw_text(window, "Необходимые ингредиенты:", 30, '#000000', (700, 220))
    
    y_offset = 270
    for ingredient in pizza_ingredients:
        color = '#00AA00' if ingredient in placed_ingredients else '#000000'
        draw_text(window, ingredient, 25, color, (700, y_offset))
        y_offset += 40
    
    # Сообщение обратной связи
    if feedback_message and pygame.time.get_ticks() - feedback_timer < MAX_FEEDBACK_TIME:
        draw_text(window, feedback_message, 25, '#FF0000', (700, 465))
    
    # Процесс выпечки
    if pizza_in_oven:
        elapsed = (pygame.time.get_ticks() - baking_start_time) / 1000
        draw_text(window, f"Время в духовке: {elapsed:.1f} сек", 30, '#000000', (850, 450))
        button_values.append(draw_button(window, 'Вытащить пиццу', 25, 850, 600, 400, 100))
    else:
        # Отображение теста и всех ингредиентов
        window.blit(testo_scaled, testo_rect.topleft)
        for i, ingredient_image in enumerate(all_ingredients_image_list):
            window.blit(ingredient_image, all_ingredients_rect_list[i].topleft)
    
    # Отображение духовки
    window.blit(oven_scaled, oven_rect.topleft)
    
    # Кнопка проверки пиццы
    if not pizza_ready:
        button_values = [draw_button(window, 'Проверить пиццу', 25, 700, 900, 400, 100)]
    else:
        draw_text(window, "Перетащите пиццу в духовку", 30, '#00AA00', (700, 900))
    
    # Кнопка перехода на следующий уровень
    if current_level < 3 and coins >= required_coins[current_level - 1]:
        button_values.append(draw_button(window, 'Новый уровень', 25, 1200, 330, 400, 100))

def game_over_scene():
    global button_values
    window.fill((0, 0, 0))
    draw_text(window, "Игра окончена", 50, '#FFFFFF', (500, 300))
    draw_text(window, feedback_message, 30, '#FFFFFF', (500, 360))
    draw_text(window, f"Вы заработали {coins} монет", 30, '#FFFFFF', (500, 420))
    draw_text(window, "Хотите продолжить?", 30, '#FFFFFF', (500, 480))
    button_values = [
        draw_button(window, "Да", 25, 500, 540, 200, 100),
        draw_button(window, "Нет", 25, 800, 540, 200, 100)
    ]
    return button_values

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Обработка меню
        if current_game_scene == 'menu':
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_values:
                    if button[0].collidepoint(event.pos):
                        if button[1] == "Начать игру":
                            reset_game()
                            current_game_scene = 'game'
                        elif button[1] == "Выйти":
                            pygame.quit()
                            sys.exit()
                            
        # Обработка игры
        elif current_game_scene == 'game':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Обработка перетаскивания готовой пиццы
                if pizza_ready and not pizza_in_oven and testo_rect.collidepoint(event.pos):
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = testo_rect.x - mouse_x
                    offset_y = testo_rect.y - mouse_y
                else:
                    # Обработка нажатия на кнопки
                    for button in button_values:
                        if button[0].collidepoint(event.pos):
                            if button[1] == "Проверить пиццу":
                                check_pizza()
                            elif button[1] == "Новый уровень":
                                if coins >= required_coins[current_level - 1]:
                                    current_level += 1
                                    start_level()
                                    feedback_message = f"Уровень {current_level} начинается!"
                                    feedback_timer = pygame.time.get_ticks()
                                else:
                                    feedback_message = "Недостаточно монет для перехода на следующий уровень"
                                    feedback_timer = pygame.time.get_ticks()
                            elif button[1] == "Вытащить пиццу" and pizza_in_oven:
                                elapsed = (pygame.time.get_ticks() - baking_start_time) / 1000
                                if elapsed >= 5 and elapsed <= 7:
                                    finish_baking()
                                else:
                                    if elapsed < 5:
                                        feedback_message = "Пицца недопечена!"
                                    else:
                                        feedback_message = "Пицца сгорела!"
                                    current_game_scene = 'game_over'
                                    pizza_in_oven = False
                    # Обработка выбора ингредиента
                    for i, rect in enumerate(all_ingredients_rect_list):
                        if rect.collidepoint(event.pos) and not pizza_ready:
                            active_ingredient = i
                            
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if dragging:
                    dragging = False
                    # Проверка, находится ли пицца над духовкой
                    if testo_rect.colliderect(oven_rect) and pizza_correct:
                        pizza_in_oven = True
                        baking_start_time = pygame.time.get_ticks()
                        testo_rect.topleft = (-1000, -1000)
                        for rect in placed_rects:
                            rect.topleft = (-1000, -1000)
                elif active_ingredient is not None:
                    # Добавление ингредиента на пиццу
                    if all_ingredients_rect_list[active_ingredient].colliderect(testo_rect) and not pizza_ready:
                        current_ingredient = ingredient_names[active_ingredient]
                        if current_ingredient in pizza_ingredients and current_ingredient not in placed_ingredients:
                            placed_ingredients.add(current_ingredient)
                            placed_rects.append(all_ingredients_rect_list[active_ingredient])
                            feedback_message = f"Добавлен {current_ingredient}"
                            feedback_timer = pygame.time.get_ticks()
                    active_ingredient = None
                    
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    testo_rect.x = event.pos[0] + offset_x
                    testo_rect.y = event.pos[1] + offset_y
                    for rect in placed_rects:
                        rect.x += event.rel[0]
                        rect.y += event.rel[1]
                elif active_ingredient is not None and not pizza_ready:
                    all_ingredients_rect_list[active_ingredient].move_ip(event.rel)
                    
        # Обработка окончания игры
        elif current_game_scene == 'game_over':
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_values:
                    if button[0].collidepoint(event.pos):
                        if button[1] == "Да":
                            reset_game()
                            current_game_scene = 'game'
                        elif button[1] == "Нет":
                            current_game_scene = 'menu'

    # Отрисовка сцены
    button_values = []
    if current_game_scene == 'menu':
        menu_scene()
    elif current_game_scene == 'game':
        game_scene()
        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time > level_times[current_level - 1]:
            feedback_message = "Время вышло!"
            current_game_scene = 'game_over'
    elif current_game_scene == 'game_over':
        game_over_scene()

    pygame.display.flip()

pygame.quit()