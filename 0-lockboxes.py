def canUnlockAll(boxes):
    # Total number of boxes
    n = len(boxes)
    
    # Set to keep track of unlocked boxes
    unlocked = [False] * n
    unlocked[0] = True  # The first box is always unlocked
    
    # Stack for DFS approach (could also use a queue for BFS)
    stack = [0]
    
    # While there are boxes to explore
    while stack:
        # Get the current box
        current_box = stack.pop()
        
        # Try to unlock boxes with keys in the current box
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    
    # Check if all boxes are unlocked
    return all(unlocked)

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes)) 

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
