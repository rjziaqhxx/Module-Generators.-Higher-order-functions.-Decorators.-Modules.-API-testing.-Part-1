def draw_horizontal_func(symbol):
    print(symbol*10)

def draw_vertical_func(symbol):
    for i in range(10):
        print(symbol)

def show_line(symbol, function_to_call):
    function_to_call(symbol)

print('Horizontal')
show_line('%',draw_horizontal_func)

print('Vertical')
show_line('%',draw_vertical_func)