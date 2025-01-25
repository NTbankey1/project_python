from drawing import *

def process_command(command, t):
    command = command.lower()
    
    try:
        
        if "vẽ hình vuông" in command:
            draw_square(t, 100)
        
        elif "vẽ hình tròn" in command:
            radius = 50
            if "bán kính" in command:
                radius = int(parts[parts.index("bán kính") + 1])
            draw_circle(t, radius)
        
        elif "vẽ đường thẳng" in command:
            t.forward(100)
        
        elif "xoay phải" in command:
            t.right(90)
        
        elif "xoay trái" in command:
            t.left(90)

        elif "vẽ hình chữ nhật" in command:
            draw_rectangle(t, 150, 100)

        elif "vẽ hình tam giác" in command:
            draw_triangle(t, 100)

        elif "vẽ hình sao" in command:
            draw_star(t, 100)

        elif "vẽ hình ngũ giác" in command:
            draw_polygon(t, 5, 100)

        elif "vẽ hình lục giác" in command:
            draw_polygon(t, 6, 100)

        elif "vẽ hình elip" in command:
            draw_ellipse(t)

        elif "vẽ đa giác kích thước" in command:
            parts = command.split()
            sides = int(parts[-2])
            size = int(parts[-1])
            draw_polygon(t, sides, size)

        else:
            print("Lệnh không được nhận diện")
    except Exception as e:
        print(f"Có lỗi xảy ra khi thực hiện lệnh vẽ: {e}") 