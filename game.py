"""Get the number"""
import numpy as np

number = np.random.randint(1, 101) #generate number

#Number of gausing
count = 0
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: "))
    if predict_number < number:
        print("Число меньше")
    elif predict_number > number:
        print("Число больше")
    else:
        print(f"Вы угадали число! Это число = {number} за {count} попыток")
        break