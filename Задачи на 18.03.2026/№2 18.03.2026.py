def simple_map(transformation, values):
    # Применяет функцию transformation к каждому элементу списка values

    result = []
    for value in values:
        result.append(transformation(value))
    return result
