# https://leetcode.com/problems/two-sum/

#Problem:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Examples:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Create a random list of unique element (set)

array = list(set(sorted([random.randint(0,20) for i in range(10)])))

target = 12

def two_sum_v1(array, target):
    """
    For each element, find the complementary value and check if this second value is in the list.
    Complexity: O(n²)
    """
    for indice, value in enumerate(array):
        second_value = target - value
        # Complexity of in is O(n). https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python
        if second_value in array:
            return [indice, array.index(second_value)]
    else:
        return None


def two_sum_v2(array, target):
    """
    Create an hashtable, try to get the complementary value of each value.
    Specifity: Get all the possible value
    Complexity: O(n²)
    """
    hashTable = {v: i for i, v in enumerate(array)}
    return [
        (i, hashTable.get(target - v))
        for i, v in enumerate(array)
        if hashTable.get(target - v, i) != i
    ]


def two_sum_v3(array, target):
    """
    A loop with two cursor that go up and down.
    If the sum of the highest and the lowest is higher than the target, Then reduce the higher cursor.
    Else the sum is lower, then increse the lower cursor.
    Complexity: O(log(n)) List must be sorted.
    """
    lower_pos = 0
    higher_pos = -1
    n = len(array)
    while lower_pos != n + higher_pos:
        temp = array[higher_pos] + array[lower_pos]
        if temp > target:
            higher_pos -= 1
        elif temp < target:
            lower_pos += 1
        else:
            return [lower_pos, n + higher_pos]
    return None


def two_sum_v4(array, target):
    """
    Create an hashtable as you go of the complementary value.
    Complexity: O(n)
    """
    look_for = {}
    for n, x in enumerate(array):
        try:
            return look_for[x], n
        except KeyError:
            look_for.setdefault(target - x, n)

two_sum_v1(array, target)
two_sum_v2(array, target)
two_sum_v3(array, target)
two_sum_v4(array, target)
