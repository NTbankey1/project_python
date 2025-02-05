import pygame
from snake import Snake
from food import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake.body)  # Khởi tạo thức ăn với thân rắn
    font = pygame.font.Font(None, 36)  # Tạo font cho thông báo
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # Xử lý sự kiện bàn phím
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 10):
                    snake.change_direction((0, -10))  # Di chuyển lên
                elif event.key == pygame.K_DOWN and snake.direction != (0, -10):
                    snake.change_direction((0, 10))  # Di chuyển xuống
                elif event.key == pygame.K_LEFT and snake.direction != (10, 0):
                    snake.change_direction((-10, 0))  # Di chuyển trái
                elif event.key == pygame.K_RIGHT and snake.direction != (-10, 0):
                    snake.change_direction((10, 0))  # Di chuyển phải

        # Di chuyển rắn
        snake.move()

        # Kiểm tra va chạm với thức ăn
        if snake.body[0] == food.position:
            snake.grow()
            food = Food(snake.body)  # Tạo thức ăn mới với thân rắn hiện tại

        # Kiểm tra va chạm với bức tường và điều chỉnh vị trí
        head_x, head_y = snake.body[0]
        if head_x < 0:  # Ra ngoài bên trái
            head_x = 390  # Xuất hiện bên phải
        elif head_x >= 400:  # Ra ngoài bên phải
            head_x = 0  # Xuất hiện bên trái
        elif head_y < 0:  # Ra ngoài bên trên
            head_y = 390  # Xuất hiện bên dưới
        elif head_y >= 400:  # Ra ngoài bên dưới
            head_y = 0  # Xuất hiện bên trên

        # Cập nhật vị trí đầu rắn
        snake.body[0] = (head_x, head_y)

        # Vẽ mọi thứ
        screen.fill((0, 0, 0))  # Màu nền
        for segment in snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))  # Vẽ rắn
        pygame.draw.rect(screen, (255, 0, 0), (food.position[0], food.position[1], 10, 10))  # Vẽ thức ăn

        # Hiển thị thông báo khi game over
        if game_over:
            text = font.render("Bên kìa!", True, (255, 255, 255))
            screen.blit(text, (150, 180))  # Vị trí hiển thị thông báo

        pygame.display.flip()
        clock.tick(15)  # Tốc độ trò chơi

if __name__ == "__main__":
    main()
