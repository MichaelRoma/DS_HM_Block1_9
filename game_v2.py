"""Угадай число"""
"""Программа автоматически угадывает число"""
import numpy as np

def random_number(number: int = 1)-> int:
    """Случайно угаданное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    low_number = 1
    hihg_number = 101
    predict_number = np.random.randint(low_number,hihg_number)
    while True:
        count += 1
        if predict_number > number:
            hihg_number = predict_number
            predict_number = np.random.randint(low_number,predict_number)
        elif predict_number < number:
            low_number = predict_number
            predict_number = np.random.randint(predict_number, hihg_number)
        else: break
    return count

def score_game(random_number)->int:
    """Считаем количство попыток необходимое для угадывания числа

    Args:
        random_predict ([type]): [description]

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size = 1000)
    for number in random_array:
        count_ls.append(random_number(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угавает число в среднем за: {score} попыток')

score_game(random_number)