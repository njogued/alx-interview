#!/usr/bin/python3
"""
Lockboxes
"""
def unlocker(box, openboxes, boxes):
    """Unclock all"""
    # [[1, 2], [2], []]
    if len(boxes) == len(openboxes):
        return
    # if len(box) == 0:
    #   return
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
    if len(boxes[0]) == 0 and len(boxes) > 1:
        # boxes = [[], [2], [3], [4], []]
        return False
    if len(boxes[0]) == 0 and len(boxes) == 1:
        # boxes = [[]]
        return True
    unlocked = unlocker(boxes[0], openboxes, boxes)
    if len(unlocked) == len(boxes):
        return True
    else:
        return False
