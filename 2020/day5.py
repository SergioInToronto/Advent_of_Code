import copy


with open('day5.input') as f:
    boarding_passes = f.read().strip().split()

def _name_me(chars, lower):
    min = 0
    max = 2 ** len(chars) - 1
    for char in chars:
        if char == lower:
            max = ((max + min + 1) / 2) - 1
        else:
            min = min + ((max + 1 - min) / 2)
    assert min == max
    return min

def _seat_id(bp):
    row = _name_me(bp[:7], 'F')
    seat = _name_me(bp[7:], 'L')
    return int(row * 8 + seat)


seat_ids = [_seat_id(x) for x in boarding_passes]
print([x for x in range(min(seat_ids), max(seat_ids) + 1) if x not in seat_ids])