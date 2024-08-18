#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = {0}  # Start with the first box unlocked
    keys = boxes[0]  # Start with the keys in the first box

    while keys:
        new_key = keys.pop()
        if new_key not in unlocked and new_key < n:
            unlocked.add(new_key)
            keys.extend(boxes[new_key])  # Add keys from the newly unlocked box

    return len(unlocked) == n  # Check if all boxes are unlocked
