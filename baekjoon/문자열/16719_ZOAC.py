alpha = input()
result = [''] * len(alpha)


def get_value(start, array):
    if not array:
        return
    min_value = min(array)
    temp = array.index(min_value)
    result[start + temp] = min_value
    print(''.join(result))
    get_value(start + temp + 1, array[temp + 1:])
    get_value(start, array[:temp])


get_value(0, list(alpha))
