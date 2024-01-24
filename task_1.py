`"""
hw
"""

if __name__ == '__main__':
    def plus_two(number):
        """
        2 + inputed number
        """
        try:
            result = 2 + int(number)
            print(result)
        except ValueError:
            print("Введите целочисленный тип данных")


    user_input = input("Введите число: ")

    plus_two(user_input)
