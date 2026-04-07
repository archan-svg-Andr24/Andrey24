import tkinter as tk
from PIL import ImageGrab

def pumpkin(filename, w, *colors):
    # Размеры изображения
    width = int(8 * w)
    height = int(5.5 * w)

    # Создаём окно и холст с белым фоном
    root = tk.Tk()
    root.title("Pumpkin")
    canvas = tk.Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    # Коэффициенты для эллипсов (в долях w)
    ellipses = [
        (4.0 - 2.2, 2.75, 0.6, 1.2),  # левый крайний
        (4.0 + 2.2, 2.75, 0.6, 1.2),  # правый крайний
        (4.0 - 1.2, 2.75, 0.9, 1.4),  # левый средний
        (4.0 + 1.2, 2.75, 0.9, 1.4),  # правый средний
        (4.0, 2.75, 1.25, 1.5)        # центральный
    ]

    pumpkin_color = colors[0] if len(colors) > 0 else '#FC0'
    for cx, cy, a, b in ellipses:
        x1 = int((cx - a) * w)
        y1 = int((cy - b) * w)
        x2 = int((cx + a) * w)
        y2 = int((cy + b) * w)
        canvas.create_oval(x1, y1, x2, y2, fill=pumpkin_color, outline=pumpkin_color)

    # Черешок (линия)
    stem_color = colors[1] if len(colors) > 1 else '#872C17'
    start_x = int(4.0 * w)
    start_y = int((2.75 - 1.5) * w)
    end_x = int((4.0 + 0.4) * w)
    end_y = int((2.75 - 1.5 - 0.3) * w)
    canvas.create_line(start_x, start_y, end_x, end_y, fill=stem_color, width=3)

    # Лист (эллипс)
    leaf_color = colors[2] if len(colors) > 2 else '#219129'
    leaf_cx = int((4.0 + 0.5) * w)
    leaf_cy = int((2.75 - 1.8) * w)
    leaf_a = int(0.3 * w)
    leaf_b = int(0.2 * w)
    x1 = leaf_cx - leaf_a
    y1 = leaf_cy - leaf_b
    x2 = leaf_cx + leaf_a
    y2 = leaf_cy + leaf_b
    canvas.create_oval(x1, y1, x2, y2, fill=leaf_color, outline=leaf_color)

    # Обновляем отрисовку и даём время на завершение
    root.update()
    # Захватываем область холста
    x0 = root.winfo_rootx() + canvas.winfo_x()
    y0 = root.winfo_rooty() + canvas.winfo_y()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()
    img = ImageGrab.grab(bbox=(x0, y0, x1, y1))
    img.save(filename)
    root.destroy()
pumpkin('img.png', 50, '#FC0', '#872C17', '#219129')