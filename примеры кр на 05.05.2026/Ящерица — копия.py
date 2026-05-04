from PIL import Image


def rotation(input_file: str, crop_coords: tuple, bg_color: str):
    # Открываем исходное изображение
    original = Image.open(input_file)
    W, H = original.size

    x, y, size = crop_coords

    # Вырезаем квадрат
    lizard = original.crop((x, y, x + size, y + size))

    # Три версии
    normal = lizard
    rotated = lizard.rotate(-90, expand=True)  # -90 = по часовой стрелке
    mirrored = lizard.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    # Если поворот меняет размер (expand=True), нужно обрезать или изменить подход
    # Но rotate на 90° с expand=True даст квадрат того же size
    # На всякий случай: если размер изменился, масштабируем
    if rotated.size != (size, size):
        rotated = rotated.resize((size, size))

    # Создаём фон
    canvas = Image.new('RGB', (W, H), bg_color)

    # Вставляем
    canvas.paste(normal, (0, 0))
    canvas.paste(rotated, ((W - size) // 2, (H - size) // 2))
    canvas.paste(mirrored, (W - size, H - size))

    # Сохраняем
    canvas.save('lizard.png')

