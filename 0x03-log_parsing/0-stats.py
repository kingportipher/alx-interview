from collections import Counter

def is_valid_line(line):
  """Checks if the line matches the expected format."""
  parts = line.strip().split()
  return len(parts) == 6 and parts[2] == 'GET' and parts[4].isdigit() and parts[5].isdigit()

def parse_line(line):
  """Extracts data from a valid line."""
  parts = line.strip().split()
  return int(parts[5])

total_size = 0
status_counts = Counter()
line_count = 0

for line in sys.stdin:
  if is_valid_line(line):
    total_size += parse_line(line)
    status_counts[int(line.split()[4])] += 1
    line_count += 1

  # Print statistics every 10 lines or on keyboard interrupt
  if line_count % 10 == 0 or line_count > 0 and not line.strip(): 
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
      print(f"{code}: {count}")
    total_size = 0
    status_counts.clear()
    line_count = 0

# Print remaining statistics on script exit (including the last 10 lines)
print(f"Total file size: {total_size}")
for code, count in sorted(status_counts.items()):
  print(f"{code}: {count}")
