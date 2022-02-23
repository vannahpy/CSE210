from pyray import *
init_window(2000, 650, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    draw_text("Hello world", 300, 300, 200, VIOLET)
    end_drawing()
close_window()