from enum import Enum

class Direction(Enum):
    RIGHT = 1,
    DOWN  = 2,
    LEFT  = 3,
    UP    = 4

def direction_generator(direction=Direction.RIGHT):
    order = [
        Direction.RIGHT,
        Direction.DOWN,
        Direction.LEFT,
        Direction.UP
    ]
    idx = (order.index(direction) + 1) % 4
    while True:
        yield order[idx]
        idx = (idx + 1) % 4
