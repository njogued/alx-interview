#!/usr/bin/python3
"""
Lockboxes
"""


def unlocker(box, openboxes, boxes):
    if len(boxes) == len(openboxes):
        return
    for value in box:
        if value >= len(boxes):
            continue
        if value not in openboxes:
            openboxes.add(value)
            unlocker(boxes[value], openboxes, boxes)
    return openboxes


def canUnlockAll(boxes):
    """Check if unlocked"""
    openboxes = {0}
    if len(boxes) == 1:
        return True
    unlocked = unlocker(boxes[0], openboxes, boxes)
    if len(unlocked) == len(boxes):
        return True
    else:
        return False
