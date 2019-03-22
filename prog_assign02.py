from math import sqrt

MAX = 20

class Data:
  def __init__(self):
    self.x = 0
    self.y = 0

local, seq, overlap = [None] * MAX, [None] * (MAX + 1), [0] * (MAX + 1)
def tour(num, len, min):
  for i in range(num):
    if (overlap[i] == overlap[num]):
      return -1;
    if min > 0 and min < len:
      return -1; 
    if num != 0:
      sqX = (local[overlap[num]].x - local[overlap[num - 1]].x)*(local[overlap[num]].x - local[overlap[num - 1]].x)
      sqY = (local[overlap[num]].y - local[overlap[num - 1]].y)*(local[overlap[num]].y - local[overlap[num - 1]].y)
      len += sqrt(sqX + sqY)
    if n - 1 == num:
      sqX = (local[overlap[num]].x - local[overlap[0]].x)*(local[overlap[num]].x - local[overlap[0]].x)
      sqY = (local[overlap[num]].y - local[overlap[0]].y)*(local[overlap[num]].y - local[overlap[0]].y)
      len += sqrt(sqX + sqY)
      if min == -1:
        min = len;
        for i in range(n):
          seq[i] = overlap[i]
      elif len < min:
        min = len
        for i in range(n):
          seq[i] = overlap[i]
      return min
  for i in range(1, n):
    overlap[num + 1] = i
    tmp = tour(num + 1, len, min)
    if min == -1 and tmp > 0:
      min = tmp; 
    elif min != -1 and tmp > 0 and tmp < min:
      min = tmp; 
  return min;

name = ['input0.txt','input1.txt','input2.txt','input3.txt','input4.txt','input5.txt','input6.txt']
for a in range(8):
  filename = name[a]
  fp = open(filename, 'r', encoding='UTF8')
  n = int(fp.readline())

  for i in range(n):
    local[i].x = local[i].x
    local[i].y = local[i].y
  fp.close()

  print("%lf\n" % tour(0, 0.0, -1))

  for i in range(n):
    print("%d " % seq[i])
  print('\n\n')