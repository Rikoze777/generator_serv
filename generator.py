for number in range(1, 1001):
    if number % 3 == 0 and number % 5 == 0:
        print("МаркоПолло")
    elif number % 3 == 0:
        print("Марко")
    elif number % 5 == 0:
        print("Полло")
    else:
        print(number)
