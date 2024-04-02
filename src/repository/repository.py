class NumberRepository:

    def get_value(self, number: int):
        if number % 3 == 0 and number % 5 == 0:
            return "МаркоПолло"
        elif number % 3 == 0:
            return "Марко"
        elif number % 5 == 0:
            return "Полло"
        else:
            return number
