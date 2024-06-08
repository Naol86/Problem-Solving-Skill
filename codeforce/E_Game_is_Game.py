class TrieNode:
  def __init__(self):
    self.children = {}
    self.is_end = False

class Main:
  def __init__(self) -> None:
    self.root = TrieNode()
  
  def insert(self, word, first):
    cur = self.root
    for i in range(len(word)):
      w = word[i]
      if i == len(word) - 1 and not cur.is_end and not first:
        return False
      if w not in cur.children:
        if not first:
          return False
        cur.children[w] = TrieNode()
      cur = cur.children[w]
    cur.is_end = True
    return True

n, k = map(int, input().split())
winner = False
ans = 1
s = input()
root = Main()
root.insert(s, True)
for i in range(1, n):
  s = input()
  if not winner:
    if not root.insert(s, False):
      ans = i % 2
      winner = True
st = ["First", "Second"]
# print(ans)
if k % 2 == 1:
  print(st[(ans + 1)%2])
else:
  print(st[ans])