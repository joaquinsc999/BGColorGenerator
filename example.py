from utils.colorgenerator import get_bg_color

text = [255, 255, 255, 1]

bg = get_bg_color(text, turn_off_visualization=True)

print(bg)
