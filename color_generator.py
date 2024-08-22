import tkinter as tk
from random import randint, shuffle
'''
- randomly select a color, R, G, or B, as the base tone
- randomly generate Base color with base tone as having a differnet range: base tone range: 200-255, normal range: 100-200
- generate 2 darker tones for Base Color:
    Method 1:
        - Generate new color: Decrease all values propotionaly by a random value between a quarter and half of the smallest RGB value of the Base Color
        - Generate new color: based on previous color, same rule set as above.
    Method 2:
        - Generate new color: unpropotionaly decrease each value by a random amount with same range as above
        - Generate new color: based on previous color, same rule set as above.
''' 
def rgb_list_to_hex(rgb_list):
    def rgb_to_hex(r, g, b):
        # Ensure each value is between 0 and 255
        if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
            raise ValueError("Each value must be between 0 and 255")
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    
    hex_list = []
    for rgb in rgb_list:
        if len(rgb) != 3:
            raise ValueError("Each RGB tuple must have exactly three elements.")
        r, g, b = rgb
        hex_list.append(rgb_to_hex(r, g, b))
    
    return hex_list

def generate_palette():
    palette_list = []

    base_color = [randint(200, 255), randint(50, 200), randint(50, 200)]
    shuffle(base_color)
    palette_list.append(base_color)

    # Method 1
    for sub_color in range(2):
        darken_value = randint(int(min(palette_list[sub_color]) / 3), int(min(palette_list[sub_color]) / 2))
        new_color = []
        for color in palette_list[sub_color]:
            new_color.append(color - darken_value)
        palette_list.append(new_color)
    
    #generate adjacent base color:
    for current_pallete_color in range(3):
        complimentary_color = []
        for color in palette_list[current_pallete_color]:
            complimentary_color.append((255-color))
        palette_list.append(complimentary_color)

    #print(palette_list)
    return rgb_list_to_hex(palette_list)

generate_palette()

def create_squares(root, colors):
    """Create squares with specified colors."""
    height = 70
    square_size = height
    margin = 10
    start_x = margin
    start_y = margin

    # Remove existing squares
    for widget in root.winfo_children():
        if isinstance(widget, tk.Canvas):
            widget.destroy()

    # Create and place the squares
    for i, color in enumerate(colors):
        square = tk.Canvas(root, width=square_size, height=square_size, bg=color, highlightthickness=0)
        square.place(x=start_x + i * square_size, y=start_y)

def update_colors(root):
    """Update the colors of the squares based on a new palette."""
    colors = generate_palette()
    create_squares(root, colors)

def create_gui():
    """Create the main GUI window with a button to update colors."""
    height = 70
    square_size = height
    width = square_size * 6  # Width is height multiplied by 6
    margin = 10  # Margin around the entire grid
    button_margin = 10  # Margin between the grid and the button

    # Create the main window
    root = tk.Tk()
    root.title("Colored Squares Grid")

    # Set window size
    window_width = width + 2 * margin
    window_height = height + 2 * margin + 40  # Extra space for the button
    root.geometry(f"{window_width}x{window_height}")

    # Create initial squares with random colors
    update_colors(root)

    # Create a button to update the colors
    update_button = tk.Button(root, text="Update Colors", command=lambda: update_colors(root))
    
    # Center the button horizontally
    button_width = update_button.winfo_reqwidth()
    button_x = (window_width - button_width) // 2
    update_button.place(x=button_x, y=height + margin + button_margin)

    # Run the application
    root.mainloop()

# Run the GUI application
create_gui()