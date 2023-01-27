import arcade
size=220;   width = 8;   height = 8;   center=20;   center_x = size//11;   center_y = size//10 
arcade.open_window(size, size, 'diamond')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
def rectangle(color): arcade.draw_rectangle_filled(center_x, center_y, width, height, color, 45)
for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            rectangle(arcade.color.RED)
        else:
            rectangle(arcade.color.BLUE)
        center_x += center
    center_x = center
    center_y += center
arcade.finish_render()
arcade.run()