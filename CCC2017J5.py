#CCC 2017 Senior 3
#Nailed It!

def find_number_of_boards_at_height(h):
  lengths = countingSort.copy()
  
  a = max(1, h - 2000)
  b = h - a
  num_of_boards = 0

  while a <= h/2:
    if a == b:
      boards = lengths[a]//2
      lengths[a] -= boards*2
      num_of_boards += boards
    else:
      boards = min(lengths[a], lengths[b])
      lengths[a] -= boards
      lengths[b] -= boards
      num_of_boards += boards

    a+=1
    b-=1

  return num_of_boards

N = int(input())
data = [int(s) for s in input().split()]
countingSort = [0]*(2001)

for datum in data:
  countingSort[datum]+=1
#print(countingSort)

max_boards = 0
heights_at_max_boards = 0
 
for i in range (2, 4000, 1):
  boards = find_number_of_boards_at_height(i)
  #print(i, boards)
  if boards > max_boards:
    max_boards = boards
    heights_at_max_boards = 0
  if boards == max_boards:
      heights_at_max_boards+=1

print(max_boards, heights_at_max_boards)


