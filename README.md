## Project Overview

The project consists of a Python function that accepts a list of lists as input, where each sublist represents a box and the numbers inside the sublist represent keys to other boxes. The goal is to determine if you can unlock all the boxes starting from the first box (`boxes[0]`).

### Requirements:
- Each box is numbered sequentially from `0` to `n-1`.
- A key with the same number as a box unlocks that box.
- All keys are positive integers.
- There can be keys that do not correspond to any box.
- The first box (`boxes[0]`) is always unlocked.

### Function Prototype:
```python
def canUnlockAll(boxes):
