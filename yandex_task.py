"""У вас есть список конфет разных типов, вам нужно собрать одинаковые наборы для своих друзей.
Какому максимальному числу друзей вы сможете собрать наборы так, чтобы раздарить все конфеты.
Реализуйте функцию на питоне, которая принимает на вход список конфет и отдает максимальное число друзей
ТЕСТ: ['a','b''c'] ОТВЕТ:1
ТЕСТ: ['a','b','c','a','b','c','d'] ОТВЕТ:1
ТЕСТ: ['a','b','c','a','b','c'] ОТВЕТ:2
"""

from math import gcd


def calculate_max_friends(candies_list):
    """
    Calculates maximum number of friends I can present the same set of candies with no candies left for myself.
    Firstly, I calculate the number of candies of each unique sort. Lastly, I return the greatest common divisor
    for these number of candies of each unique sort. That's the answer, it's the maximum number of friends I can
    present the same sets of candies with no candies left for myself
    :param candies_list:
    :return int:
    """
    candy_duplicates = [candies_list.count(i) for i in set(candies_list)]
    return gcd(*candy_duplicates)


if __name__ == '__main__':
    candies = ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b']

    assert calculate_max_friends(['a', 'b', 'c', 'a', 'b', 'c']) == 2
    assert calculate_max_friends(['a', 'b', 'c', 'a', 'b', 'c', 'd']) == 1
    assert calculate_max_friends(['a', 'b', 'c']) == 1
    assert calculate_max_friends(['a', 'b', 'c', 'a', 'b', 'c', 'a', 'a']) == 2
    assert calculate_max_friends(['a', 'a', 'a', 'b', 'a', 'a', 'b']) == 1
    assert calculate_max_friends(['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b']) == 3

    result = calculate_max_friends(candies)
    print(result)
