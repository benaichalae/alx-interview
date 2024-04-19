#!/usr/bin/python3
"""Lockboxes task"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened given a list of keys for each box.

    Args:
        boxes: A list of lists, where each inner list represents the keys
        available to open that box (indexed by its position).

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    opened = set([0])
    remaining = set(range(1, len(boxes)))

    while remaining:
        new_opened = set()
        for box in opened:
            for key in boxes[box]:
                if 0 <= key < len(boxes) and key in remaining:
                    new_opened.add(key)
                    remaining.remove(key)
        if not new_opened:
            return False
        opened.update(new_opened)

    return not remaining
