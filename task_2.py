"""
hw
"""

if __name__ == "__main__":
    def access_array_element(arr, index):
        """
        принимает массив и индекс
        """
        try:
            value = arr[index]
            print("Значение элемента с индексом", index, ":", value)
        except IndexError:
            print("Индекс выходит за границы массива!")


    my_array = [1, 2, 3, 4, 5]

    access_array_element(my_array, 10)
    access_array_element(my_array, -1)
