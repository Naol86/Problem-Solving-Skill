player, queries = map(int, input().split())

parent = [i for i in range(player)]
players = [[i] for i in range(player)]
experience = [0] * player
representation = [0] * player

def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def update(x, y):
  for j in range(len(players[y])):
    experience[players[y][j]] += representation[y] - representation[x]
  players[x].extend(players[y])
  # representation[x] = 0
  representation[y] = 0
  players[y] = []

def union(x, y):
  par_x = find(x)
  par_y = find(y)
  if par_x != par_y:
    if players[par_x] > players[par_y]:
      parent[par_y] = par_x
      update(par_x, par_y)
    else:
      parent[par_x] = par_y
      update(par_y, par_x)

for _ in range(queries):
  cmd = input().split()
  if cmd[0] == 'join':
    union(int(cmd[1]) - 1, int(cmd[2]) - 1)
  elif cmd[0] == 'add':
    par = find(int(cmd[1]) - 1)
    representation[par] += int(cmd[2])
  else:
    par = find(int(cmd[1]) - 1)
    print(experience[int(cmd[1]) - 1] + representation[par])