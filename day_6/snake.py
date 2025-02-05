# snake.py

import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)  # Bắt đầu di chuyển sang phải

    def move(self):
        # Di chuyển rắn
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()  # Xóa đuôi

    def grow(self):
        # Tăng kích thước rắn
        self.body.append(self.body[-1])  # Thêm một phần vào đuôi

    def change_direction(self, new_direction):
        # Thay đổi hướng di chuyển
        self.direction = new_direction