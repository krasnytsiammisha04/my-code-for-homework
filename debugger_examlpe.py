"""
В нас є список [1, 2 , 3, 4, 5, 9]
потрібно написати функцію, яка буде проходити по цьому списку та виводити лише парні числа
"""


# print_odd_numbers
def print_only_odd_numbers_in_a_list(number_list):
    # пройтися по усім числам
    for number in number_list:
        # перевірити чи конкретне число є парнее чи ні
        if number % 2 != 0:
            # якщо не парне, то вивести у термінал
            print(number)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_only_odd_numbers_in_a_list(numbers)
