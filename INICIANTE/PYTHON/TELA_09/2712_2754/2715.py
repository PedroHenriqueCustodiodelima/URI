import sys

for line in sys.stdin:
  size = int(line.strip())
  if size is None:
    break

  assignments = list(map(int, input().split()))

  sum_half = sum(assignments) / 2
  rangel = 0
  gugu = 0

  for r in range(len(assignments)):
    rangel += assignments[r]
    if rangel > sum_half:
      break

  not_done = assignments[r:]
  for element in not_done:
    gugu += element

  if gugu > rangel:
    gugu -= not_done[0]
  else:
    rangel -= not_done[0]

  print(abs(rangel - gugu))