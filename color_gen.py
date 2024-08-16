import random
import string

def generate_colors(color_type, n):
    colors_list = []
    
    if color_type.lower() == 'hex':
        for _ in range(n):
            hexa = ''.join(random.choice(string.hexdigits) for _ in range(6)).lower()
            hex_color = f"#{hexa}"
            colors_list.append(hex_color)
        return f"{n} Hex colors are - {colors_list}"
    
    elif color_type.lower() == 'rgb':
        for _ in range(n):
            rgb_color = tuple(random.randint(0, 255) for _ in range(3))
            colors_list.append(rgb_color)
        return f"{n} RGB colors are - {colors_list}"

print(generate_colors('hex', 3))  # Generate 3 hex colors
print(generate_colors('rgb', 2))  # Generate 2 RGB colors
