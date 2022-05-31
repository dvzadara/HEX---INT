def hex_to_big_endian(hex_value):
    """
    Превращение hex значения в big endian значение
    hex_value: hex значение
    return: big endian значение
    """
    big_endian = 0
    i = 0
    while hex_value:
        big_endian += (hex_value & 255) << i
        hex_value = hex_value >> 8
        i += 8
    return big_endian


def hex_to_little_endian(hex_value):
    """
    Превращение hex значения в little endian значение
    hex_value: hex значение
    return: little endian значение
    """
    little_endian = 0
    while hex_value:
        little_endian = little_endian << 8
        little_endian += (hex_value & 255)
        hex_value = hex_value >> 8
    return little_endian


def little_endian_to_hex(little_endian):
    """
    Превращение little endian значения в hex значение
    little_endian: little endian значение
    return: hex значение
    """
    return hex(little_endian)


def big_endian_to_hex(big_endian):
    """
    Превращение big endian значения в hex значение
    big_endian: big endian значение
    return: hex значение
    """
    hex_value = 0
    while big_endian:
        hex_value = hex_value << 8
        hex_value += 255 & (big_endian)
        big_endian = big_endian >> 8
    return hex(hex_value)


# Тесты
if __name__ == "__main__":
    hex_value = int(input("Введите hex значение: "), 16)
    print("Little endian: ", hex_to_little_endian(hex_value))
    print("Big endian: ", hex_to_big_endian(hex_value))
    little_endian = int(input("Введите little endian значение: "))
    print("Hex: ", little_endian_to_hex(little_endian))
    big_endian = int(input("Введите big endian значение: "))
    print("Hex: ", big_endian_to_hex(big_endian))

