#!/usr/bin/python3

def canUnlockAll(boxes):
  """Determines if all boxes can be opened.

  Args:
    boxes: A list of lists representing boxes and their keys.

  Returns:
    True if all boxes can be opened, False otherwise.
  """

  num_boxes = len(boxes)
  visited = [False] * num_boxes
  visited[0] = True  # First box is unlocked

  def dfs(box_index):
    for key in boxes[box_index]:
      if 0 <= key < num_boxes and not visited[key]:
        visited[key] = True
        dfs(key)

  dfs(0)
  return all(visited)
