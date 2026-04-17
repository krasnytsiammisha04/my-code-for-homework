"""
В нас є список [1, 2 , 3, 4, 5, 9]
потрібно написати функцію, яка буде проходити по цьому списку та виводити лише парні числа
"""


def is_odd(number: int) -> bool:
    """
    Function that receives a number and returns if it is odd
    """
    # if number & 2 != 0:
    #     return True
    # else:
    #     return False
    return number & 2 != 0


# print_odd_numbers
def print_odd_numbers(number_list: list[int]) -> None:
    """
    A function that receives a list of numbers and prints only odd numbers
    """
    # пройтися по усім числам
    for number in number_list:
        # перевірити чи конкретне число є парнее чи ні
        if number % 2 != 0:
            # якщо не парне, то вивести у термінал
            print(number)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_odd_numbers(numbers)

# print(is_odd("Hello"))
print_odd_numbers({1, 2, 3, 4, 5})
