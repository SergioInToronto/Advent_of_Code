raw = '12,1,16,3,11,0'


def _indexes_of(li, value):
    start_index = 0
    indexes = []
    try:
        while True:
            indexes.append(li.index(value, start_index))
            start_index = indexes[-1] + 1
    except ValueError:
        pass
    return indexes


numbers = [int(x) for x in raw.split(',')]
for i in range(len(numbers), 2020):
    indexes = _indexes_of(numbers, numbers[-1])
    assert indexes
    if len(indexes) == 1:
        numbers.append(0)
    else:
        turns_since_last_appearance = i - 1 - indexes[-2]
        assert turns_since_last_appearance > 0
        numbers.append(turns_since_last_appearance)

print(numbers[-1])
