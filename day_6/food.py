# food.py

import random

class Food:
    def __init__(self, snake_body):
        self.position = self.spawn_food(snake_body)

    def spawn_food(self, snake_body):
        while True:
            new_position = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)
            if new_position not in snake_body:  # Đảm bảo thức ăn không trùng với thân rắn
                return new_position