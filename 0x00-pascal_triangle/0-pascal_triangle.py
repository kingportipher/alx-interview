#!/usr/bin/python3

def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to the nth row.

  Args:
      n: An integer representing the number of rows in the triangle.

  Returns:
      A list of lists of integers representing Pascal's triangle.
      Returns an empty list if n <= 0.
  """
  if n <= 0:
    return []

  triangle = []
  # First row is always [1]
  triangle.append([1])

  # Iterate for remaining rows
  for i in range(1, n):
    # Initialize current row with 1
    current_row = [1]
    # Calculate values based on previous row
    for j in range(1, i):
      previous_row = triangle[i-1]
      current_row.append(previous_row[j-1] + previous_row[j])
    # Add 1 to the end of the current row
    current_row.append(1)
    # Append the completed current row to the triangle
    triangle.append(current_row)

  return triangle
