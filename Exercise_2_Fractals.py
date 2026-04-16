import tkinter as tk
import math


#question 1 triangle

def draw_sierpinski(canvas, x, y, size, depth):
    if depth == 0:
        canvas.create_polygon(
            x, y,
            x + size, y,
            x + size / 2, y - size * 0.866,
            fill='black'
        )
    else:
        new_size = size / 2
        # Bottom-left triangle
        draw_sierpinski(canvas, x, y, new_size, depth - 1)
        # Bottom-right triangle
        draw_sierpinski(canvas, x + new_size, y, new_size, depth - 1)
        # Top triangle
        draw_sierpinski(canvas, x + new_size/2, y - new_size * 0.866, new_size, depth - 1)



# Test case 
root = tk.Tk()
root.title("Depth 3 - Sierpinski Triangle")
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()
draw_sierpinski(canvas, 50, 550, 500, 3)
root.mainloop()



#question 2 tree
def draw_tree(canvas, x, y, length, angle, depth):
    if depth == 0:
        x2 = x + length * math.cos(math.radians(angle))
        y2 = y - length * math.sin(math.radians(angle))
        canvas.create_line(x, y, x2, y2, fill='green')
    else:
        x2 = x + length * math.cos(math.radians(angle))
        y2 = y - length * math.sin(math.radians(angle))
        canvas.create_line(x, y, x2, y2, fill='brown')
        draw_tree(canvas, x2, y2, length * 0.7, angle + 30, depth - 1)
        draw_tree(canvas, x2, y2, length * 0.7, angle - 30, depth - 1)


root = tk.Tk()
root.title("Depth 7 - full bushy tree")
canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.pack()
draw_tree(canvas, 400, 750, 200, 90, 7)
root.mainloop()


#question 3 dimensions
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def fractal_dimension(fractal_image, box_sizes):
    if fractal_image.ndim == 3:
        image = np.mean(fractal_image, axis=2)
    else:
        image = fractal_image

    binary = image < 128

    counts = []
    for size in box_sizes:
        count = 0
        for i in range(0, binary.shape[0], size):
            for j in range(0, binary.shape[1], size):
                box = binary[i:i+size, j:j+size]
                if box.any():
                    count += 1
        counts.append(count)

    log_sizes = np.log(1 / np.array(box_sizes))
    log_counts = np.log(counts)

    slope, intercept = np.polyfit(log_sizes, log_counts, 1)

    plt.figure()
    plt.plot(log_sizes, log_counts, 'o-')
    plt.xlabel("log(1/size)")
    plt.ylabel("log(count)")
    plt.title(f"Fractal Dimension ≈ {slope:.3f}")
    plt.grid(True)
    plt.show()

    return slope

from PIL import Image, ImageDraw
import numpy as np

def make_sierpinski_image(size=512, depth=6):
    img = Image.new('L', (size, size), 255)
    draw = ImageDraw.Draw(img)

    def draw_tri(x, y, s, d):
        if d == 0:
            draw.polygon([x, y, x+s, y, x+s//2, y-int(s*0.866)], fill=0)
        else:
            h = s // 2
            draw_tri(x, y, h, d-1)
            draw_tri(x+h, y, h, d-1)
            draw_tri(x+h//2, y-int(h*0.866), h, d-1)

    draw_tri(50, 480, 420, depth)
    return np.array(img)

image = make_sierpinski_image(depth=5)
box_sizes = [2, 4, 8, 16, 32, 64]
dim = fractal_dimension(image, box_sizes)
print(f"Sierpinski dimension: {dim:.3f}")


solid_square = np.zeros((256, 256))
box_sizes = [2, 4, 8, 16, 32]
dim = fractal_dimension(solid_square, box_sizes)
print(f"Solid square dimension: {dim:.3f}")

line_image = np.ones((256, 256), dtype=np.uint8) * 255
line_image[128, :] = 0
box_sizes = [2, 4, 8, 16, 32]
dim = fractal_dimension(line_image, box_sizes)
print(f"Straight line dimension: {dim:.3f}")